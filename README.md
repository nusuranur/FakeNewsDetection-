# 📰 Fake News Detection

This is a **Machine Learning-based Fake News Detection system** with an interactive **Streamlit web application**. It allows users to input news articles and instantly check whether they are **Real** or **Fake**, via a clean, newspaper-themed interface.

---

## 📌 Project Description

The Fake News Detection project is designed to identify and classify news articles as **real** or **fake** using machine learning techniques.

### 🔧 Core Components:

1. **Data Preprocessing:**  
   - Text cleaned, lowercased  
   - Vectorized using **TF-IDF (Term Frequency–Inverse Document Frequency)**

2. **Machine Learning Model:**  
   - A **Logistic Regression** classifier trained on labeled news articles

3. **Deployment:**  
   - Model & vectorizer serialized with **Joblib**  
   - Web app built using **Streamlit**

---

## 🔄 Workflow Overview

1. 📝 User pastes a news article into the text area  
2. 🔍 Text is cleaned and vectorized  
3. 🤖 ML model predicts whether the news is **Fake** or **Real**  
4. 🎯 Result is displayed in a stylish result box (🟥 Fake, 🟩 Real)

<div align="center">
  <img src="workflow.jpg"" width="45%" alt="Web Interface 1"/>
  &nbsp;&nbsp;
</div>

---

## ✨ Features

- ✅ Detects fake news using Logistic Regression  
- ✍️ Simple user input via text box  
- 📰 Newspaper-style web UI with **Streamlit**  
- 🔢 Feature extraction with **TF-IDF Vectorizer**  
- 💾 Model & vectorizer saved using **Joblib**

---

## 🧠 Tech Stack

| Category              | Tools / Technologies                      |
|----------------------|-------------------------------------------|
| Programming Language | Python 3.10+                              |
| ML & Data Processing | Scikit-learn, Pandas, NumPy               |
| Web App              | Streamlit                                 |
| Serialization        | Joblib                                    |
| UI Styling           | HTML, CSS                                 |


---

## 📂 Dataset Download

The dataset files `fake.csv` and `real.csv` are included in the following ZIP archive:

🔗 TRUE - [Download dataset.zip](truezip.zip)
🔗 FALSE - [Download dataset.zip](Fake.zip)

 --

## Group Members

| Name                 | Student ID |
| -------------------- | ---------- |
| Nusura Nur Nowrin    | C223283    |
| Sohain Tabassum Biva | C223280    |

## 📊 Screenshots
## 📊 Screenshots Web App Interface

<div align="center">
  <img src="outputreal.jpg"" width="45%" alt="Web Interface 1"/>
  &nbsp;&nbsp;
  <img src="outputfake.jpg"" width="45%" alt="Web Interface 2"/>
</div>

### 🔹 Prediction Output 

<div align="center">
  <img src="prediction.jpg"" width="45%" alt="Web Interface 1"/>
  &nbsp;&nbsp;
</div>


---

## 📄 Project Report

You can read the full project report here:  
[📘 View Project_Report.pdf](AIProjectreport.pdf)
If you can’t access this, please download it first, then you’ll be able to view it.

## 🚀 Getting Started

### 🔧 Install Requirements

## Installation

Step-by-step instructions to install and run the Fake News Detection project locally:

```bash
# Clone the repository
git clone https://github.com/nusuranur/Fake-News-Detection.git

# Navigate into the project directory
cd Fake-News-Detection

# (Optional) Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the required Python packages
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
## Live Demo

Check out the Fake News Detection app live here:  
[https://fake-news-detector4.streamlit.app/](https://fake-news-detector4.streamlit.app/)
