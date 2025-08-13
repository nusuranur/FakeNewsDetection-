import streamlit as st
import joblib

# Load the vectorsizer and model
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
    .stTextArea label {
        font-size: 1.8em !important; /* Larger and more visible */
        color: #4A2C2A !important; /* Match title color */
        font-weight: bold !important; /* Bolder text */
        margin-bottom: 10px !important; /* More space below label */
        display: block !important; /* Ensures it takes up full width */
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
        transform: scale(1.02); /* Slightly less aggressive scale on hover */
        background-color: #5D4037; /* Darker shade on hover */
    }

    /* Success message with solid color - CRITICAL FIX */
    /* Target the direct child div of stSuccess and apply solid background, white text */
    .stSuccess > div {
        background-color: #6D4C41 !important; /* Use the button's warm brown for "Real" news */
        color: white !important; /* White text for visibility */
        font-size: 1.5em !important;
        padding: 20px !important;
        border-radius: 8px !important;
        text-align: center !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important; /* Keep shadow for depth */
        border: none !important; /* Ensure no border interferes */
    }

    /* Error message with solid, vibrant color - CRITICAL FIX */
    /* Target the direct child div of stError and apply solid red, white text */
    .stError > div {
        background-color: #D32F2F !important; /* Deeper, solid red for "Fake" news */
        color: white !important; /* White text for high contrast */
        font-size: 1.8em !important;
        font-weight: bold !important;
        padding: 25px !important;
        border-radius: 8px !important;
        animation: fadeIn 1s !important;
        text-align: center !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important; /* Keep shadow for depth */
        border: none !important; /* Ensure no border interferes */
    }

    /* Warning message (text only, no box) */
    .stWarning {
        background-color: transparent !important;
        color: #F9A825 !important;
        font-size: 1.2em !important;
        padding: 10px 0 !important;
        border-radius: 0 !important;
        animation: fadeIn 1s !important;
        text-align: center !important;
        font-weight: bold !important;
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
        .stTextArea label {
            font-size: 1.4em !important;
        }
        .stTextArea textarea {
            height: 150px;
        }
        .stButton button {
            padding: 10px 20px;
            font-size: 1em;
        }
        .stError > div, .stSuccess > div {
            font-size: 1.4em !important;
            padding: 15px !important;
        }
        .stWarning {
            font-size: 1em !important;
            padding: 5px 0 !important;
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

if st.button("Check News"):
    if inputn.strip(): # Check if the input is not just whitespace
        with st.spinner("Analyzing..."):
            transform_input = vectorsizer.transform([inputn])
            prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("The News is Real!")
        else:
            st.error("The News is Fake!")
    else:
        st.warning("Please enter some text to analyze.")