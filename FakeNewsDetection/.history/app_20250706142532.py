from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
news_dataset = pd.read_csv('your_dataset.csv')  # Replace with your file name if different
print("Available columns:", news_dataset.columns.tolist())

# Prepare data
X = news_dataset['text']
y = news_dataset['label']
le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_vectorized = vectorizer.fit_transform(X_train)
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Save the model, vectorizer, and label encoder
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(le, 'label_encoder.pkl')
print("Model, vectorizer, and label encoder saved!")

# Flask app
from flask import Flask, request, render_template_string
import numpy as np

app = Flask(__name__)

# Load saved model, vectorizer, and label encoder
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
le = joblib.load('label_encoder.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        text = request.form['text']
        X_new = vectorizer.transform([text])
        prediction = model.predict(X_new)[0]
        prediction = le.inverse_transform([prediction])[0]
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>News Authenticity Checker</h1>
            <form method="post">
                <textarea name="text" rows="4" cols="50"></textarea><br>
                <input type="submit" value="Predict">
            </form>
            {% if prediction %}
                <h2>Prediction: {{ prediction }}</h2>
            {% endif %}
        </body>
        </html>
    ''', prediction=prediction)

if __name__ == '__main__':
    app.run(port=5000, debug=True)