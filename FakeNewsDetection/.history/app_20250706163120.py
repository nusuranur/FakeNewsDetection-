import streamlit as st
import joblib
from datetime import datetime

# Load the vectorsizer and model
# Ensure 'vectorsizer.jb' and 'lr_model.jb' are in the same directory as your app.py
try:
    vectorsizer = joblib.load("vectorsizer.jb")
    model = joblib.load("lr_model.jb")
except FileNotFoundError:
    st.error("Error: Model or vectorsizer file not found. Please ensure 'vectorsizer.jb' and 'lr_model.jb' are in the correct directory.")
    st.stop() # Stop the app if essential files are missing

# Get current date for dateline
current_date = datetime.now().strftime("%B %d, %Y").upper()
current_city = "CHATTOGRAM, BANGLADESH" # Based on our current context

# Custom CSS and HTML for newspaper theme with improved design
st.markdown(
    f"""
    <style>
    /* Newspaper background */
    .stApp {{
        background-image: url('https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #2E2E2E; /* Dark gray text */
    }}

    /* Content container */
    .content {{
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white */
        padding: 20px;
        border: 2px solid #A1887F; /* Warm brown border */
        border-radius: 10px;
        margin: 20px auto;
        max-width: 800px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Georgia', serif;
    }}

    /* Title styling */
    h1 {{
        font-size: 2.5em;
        color: #4A2C2A; /* Rich dark red for header */
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid #A1887F; /* Matching border color */
        padding-bottom: 10px;
        margin-bottom: 0px !important; /* Adjust margin below title for dateline */
    }}

    /* Dateline styling */
    .dateline {{
        text-align: center;
        font-size: 0.9em;
        font-style: italic;
        color: #5D4037; /* Slightly darker brown */
        margin-top: 5px;
        margin-bottom: 15px;
        border-bottom: 1px dashed #A1887F; /* Subtle dashed line */
        padding-bottom: 10px;
    }}

    /* Text area label styling */
    .stTextArea label p {{ /* Target the <p> tag within the label */
        font-size: 1.8em !important; /* Larger font size */
        color: #4A2C2A !important; /* Stronger, dark color */
        font-weight: bold !important; /* Make it bold */
        margin-bottom: 10px !important;
        display: block !important;
        background-color: transparent !important; /* Ensure no background */
        padding: 0 !important; /* Remove any default padding */
    }}

    /* Text area styling */
    .stTextArea textarea {{
        width: 100%;
        height: 200px;
        font-size: 1.1em;
        padding: 10px;
        border: 2px solid #A1887F;
        border-radius: 5px;
        resize: vertical;
        background-color: white !important;
        color: black !important;
        opacity: 1 !important;
        -webkit-text-fill-color: black !important;
    }}

    /* Button styling */
    .stButton button {{
        background-color: #6D4C41; /* Warm brown button */
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        transition: transform 0.3s, background-color 0.3s;
        width: 100%; /* Make button full width */
        margin-top: 15px;
        margin-bottom: 10px; /* Space between buttons if multiple */
    }}
    .stButton button:hover {{
        transform: scale(1.02);
        background-color: #5D4037; /* Darker shade on hover */
    }}

    /* Custom result box styling */
    .result-box {{
        background-color: #6D4C41; /* Default to warm brown, similar to button */
        color: white;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        margin-top: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5); /* Stronger shadow */
        font-size: 1.8em; /* Larger text */
        font-weight: bold;
        animation: fadeIn 1s ease-out; /* Smooth fade-in */
        border: 2px solid #A1887F; /* Keep the consistent border */
    }}

    .result-box.fake {{ /* Specific style for 'Fake' */
        background-color: #D32F2F; /* Deep red for fake news */
    }}

    .result-label {{
        font-size: 0.8em; /* Smaller for the label */
        font-weight: normal;
        margin-bottom: 5px; /* Space between label and result */
        opacity: 0.8;
    }}

    /* Streamlit's default info, success, warning, error containers */
    /* Ensuring they don't interfere with our custom result box */
    .stAlert {{
        padding: 0 !important;
        border: none !important;
        background-color: transparent !important;
        margin: 0 !important;
        box-shadow: none !important;
    }}
    .stAlert > div {{ /* Target the first direct child div of the alert container */
        padding: 0 !important;
        margin: 0 !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}
    .stAlert > div > div {{ /* Target the second direct child div */
        padding: 0 !important;
        margin: 0 !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}

    /* Keep the stWarning for the "empty input" message clear */
    .stWarning {{
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
    }}

    /* Expander styling (for About section) */
    .stExpander {{
        margin-top: 30px;
        border: 1px solid #A1887F; /* Matching border */
        border-radius: 8px;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.8); /* Slightly transparent white */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}
    .stExpander button {{ /* Style for the expander toggle button */
        background-color: #A1887F !important; /* Lighter brown for expander button */
        color: white !important;
        padding: 8px 15px !important;
        border-radius: 5px !important;
        width: auto !important; /* Don't make full width */
        font-size: 0.9em !important;
        transition: background-color 0.3s;
    }}
    .stExpander button:hover {{
        background-color: #8D6E63 !important; /* Darker on hover */
    }}
    .stExpander div[data-testid="stExpanderContents"] {{ /* Content inside expander */
        padding-top: 15px;
        color: #4A2C2A; /* Dark text for readability */
        font-size: 0.95em;
        line-height: 1.6;
    }}
    .stExpander h2 {{ /* Expander header text */
        color: #4A2C2A !important;
        font-size: 1.3em !important;
        font-weight: bold !important;
        margin-bottom: 10px !important;
    }}


    /* Animation for fade-in effect */
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    /* Responsive design */
    @media (max-width: 600px) {{
        .content {{
            margin: 10px;
            padding: 10px;
        }}
        h1 {{
            font-size: 2em;
        }}
        .dateline {{
            font-size: 0.8em;
        }}
        .stTextArea label p {{
            font-size: 1.4em !important;
        }}
        .stTextArea textarea {{
            height: 150px;
        }}
        .stButton button {{
            padding: 10px 20px;
            font-size: 1em;
        }}
        .result-box {{
            font-size: 1.4em;
            padding: 15px;
            margin-top: 20px;
        }}
        .stExpander {{
            margin-top: 20px;
        }}
        .stExpander h2 {{
            font-size: 1.1em !important;
        }}
    }}
    </style>
    <div class="content">
        <h1>Fake News Detector</h1>
        <p class="dateline">{current_city} – {current_date}</p>
        <p style="text-align: center; font-style: italic; color: #5D4037;">Enter a News Article below to check its authenticity.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# App content
# Use st.session_state to manage the text area content for the clear button
if 'text_input_value' not in st.session_state:
    st.session_state.text_input_value = ""

inputn = st.text_area("News Article:", value=st.session_state.text_input_value, key="news_article_input")

# Create an empty placeholder for the result
result_placeholder = st.empty()

# --- Buttons Layout ---
col1, col2 = st.columns(2) # Create two columns for buttons

with col1:
    if st.button("Check News", key="check_news_btn"):
        if inputn.strip(): # Check if the input is not just whitespace
            with st.spinner("Analyzing..."):
                transform_input = vectorsizer.transform([inputn])
                prediction = model.predict(transform_input)

            if prediction[0] == 1:
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
            result_placeholder.empty() # Clear the result box if input is empty
            st.warning("Please enter some text to analyze.")

with col2:
    # Clear button functionality
    if st.button("Clear Input", key="clear_input_btn"):
        st.session_state.text_input_value = "" # Reset text area value
        result_placeholder.empty() # Clear the displayed result
        st.experimental_rerun() # Rerun to reflect the cleared text area

# --- About This Detector Section ---
with st.expander("About This Detector"):
    st.markdown("""
        <p style="color: #4A2C2A;">
        This Fake News Detector is a demonstration project that uses a Machine Learning model to classify news articles as 'Real' or 'Fake'.
        </p>
        <p style="color: #4A2C2A;">
        It employs a <b>Logistic Regression</b> model trained on a dataset of various news articles. The text input is processed using a <b>Tf-idf Vectorsizer</b> to convert text into numerical features that the model can understand.
        </p>
        <p style="color: #4A2C2A;">
        <b>Disclaimer:</b> This tool is for demonstration purposes only and should not be used as the sole source for verifying news authenticity. Real-world news verification requires critical thinking and cross-referencing multiple reputable sources.
        </p>
        <p style="text-align: right; font-size: 0.8em; color: #5D4037;">
        Developed by [<B>Nowrin & Biva</b>]
        </p>
    """, unsafe_allow_html=True)