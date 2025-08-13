import streamlit as st
import joblib

# Load the vectorsizer and model
# Ensure 'vectorsizer.jb' and 'lr_model.jb' are in the same directory as your app.py
try:
    vectorsizer = joblib.load("vectorsizer.jb")
    model = joblib.load("lr_model.jb")
except FileNotFoundError:
    st.error("Error: Model or vectorsizer file not found. Please ensure 'vectorsizer.jb' and 'lr_model.jb' are in the correct directory.")
    st.stop() # Stop the app if essential files are missing

# Custom CSS and HTML for newspaper theme with improved design
st.markdown(
    """
    <style>
    /* Newspaper background */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #2E2E2E; /* Dark gray text */
    }

    /* Content container */
    .content {
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white */
        padding: 20px;
        border: 2px solid #A1887F; /* Warm brown border */
        border-radius: 10px;
        margin: 20px auto;
        max-width: 800px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Georgia', serif;
    }

    /* Title styling */
    h1 {
        font-size: 2.5em;
        color: #4A2C2A; /* Rich dark red for header */
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid #A1887F; /* Matching border color */
        padding-bottom: 10px;
    }

    /* Text area label styling */
    .stTextArea label p { /* Target the <p> tag within the label */
        font-size: 1.8em !important; /* Larger font size */
        color: #4A2C2A !important; /* Stronger, dark color */
        font-weight: bold !important; /* Make it bold */
        margin-bottom: 10px !important;
        display: block !important;
        background-color: transparent !important; /* Ensure no background */
        padding: 0 !important; /* Remove any default padding */
    }

    /* Text area styling */
    .stTextArea textarea {
        width: 100%;
        height: 200px; /* Larger text box */
        font-size: 1.1em;
        padding: 10px;
        border: 2px solid #A1887F; /* Consistent border */
        border-radius: 5px;
        resize: vertical; /* Allow vertical resizing */
        background-color: white !important; /* Explicitly set white background */
        color: black !important; /* Explicitly set black text color */
        opacity: 1 !important; /* Ensure no hidden opacity */
        -webkit-text-fill-color: black !important; /* For webkit browsers if color is an issue */
    }

    /* Button styling */
    .stButton button {
        background-color: #6D4C41; /* Warm brown button */
        color: white;
        padding: 12px 25px; /* Larger padding */
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        transition: transform 0.3s, background-color 0.3s;
        width: 100%; /* Make button full width for better visibility */
        margin-top: 15px; /* Add some space above the button */
    }
    .stButton button:hover {
        transform: scale(1.02);
        background-color: #5D4037; /* Darker shade on hover */
    }

    /* Custom result box styling (NEW) */
    .result-box {
        background-color: #6D4C41; /* Default to warm brown, similar to button */
        color: white;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin-top: 25px; /* More space above */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5); /* Stronger shadow */
        font-size: 1.8em; /* Larger text */
        font-weight: bold;
        animation: fadeIn 1s ease-out; /* Smooth fade-in */
        border: 2px solid #A1887F; /* Keep the consistent border */
    }

    .result-box.fake { /* Specific style for 'Fake' */
        background-color: #D32F2F; /* Deep red for fake news */
    }

    .result-label {
        font-size: 0.8em; /* Smaller for the label */
        font-weight: normal;
        margin-bottom: 5px; /* Space between label and result */
        opacity: 0.8;
    }

    /* Warning message (text only, no box) - using existing .stWarning */
    .stWarning {
        background-color: transparent !important;
        color: #F9A825 !important;
        font-size: 1.2em !important;
        padding: 10px 0 !important;
        border-radius: 0 !important;
        animation: fadeIn 1.5s !important;
        text-align: center !important;
        font-weight: bold !important;
        margin-top: 15px !important;
        -webkit-text-fill-color: #F9A825 !important;
    }

    /* Animation for fade-in effect */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Responsive design */
    @media (max-width: 600px) {
        .content {
            margin: 10px;
            padding: 10px;
        }
        h1 {
            font-size: 2em;
        }
        .stTextArea label p {
            font-size: 1.4em !important;
        }
        .stTextArea textarea {
            height: 150px;
        }
        .stButton button {
            padding: 10px 20px;
            font-size: 1em;
        }
        .result-box {
            font-size: 1.4em;
            padding: 15px;
            margin-top: 20px;
        }
    }
    </style>
    <div class="content">
        <h1>Fake News Detector</h1>
        <p style="text-align: center; font-style: italic; color: #5D4037;">Enter a News Article below to check its authenticity.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# App content
inputn = st.text_area("News Article:", "")

# Create an empty placeholder for the result
# This placeholder will be updated dynamically
result_placeholder = st.empty()

if st.button("Check News"):
    if inputn.strip(): # Check if the input is not just whitespace
        with st.spinner("Analyzing..."):
            transform_input = vectorsizer.transform([inputn])
            prediction = model.predict(transform_input)

        if prediction[0] == 1:
            # Display result in the custom-styled box
            result_placeholder.markdown(
                f"""
                <div class="result-box">
                    <div class="result-label">Result:</div>
                    The News is Real!
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Display result in the custom-styled box with 'fake' class
            result_placeholder.markdown(
                f"""
                <div class="result-box fake">
                    <div class="result-label">Result:</div>
                    The News is Fake!
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        # Clear any previous result and show warning
        result_placeholder.empty() # Clear the result box if input is empty
        st.warning("Please enter some text to analyze.")