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

    /* Text area label styling - IMPROVED */
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

    /* Success message with solid color - IMPROVED */
    .stSuccess > div { /* Target the inner div of st.success for background */
        background-color: #6D4C41 !important; /* Warm brown, fully opaque */
        color: white !important; /* White text */
        font-size: 1.5em !important; /* Slightly larger */
        padding: 20px !important; /* More padding */
        border-radius: 8px !important; /* Slightly more rounded corners */
        text-align: center !important; /* Center the text */
        margin-top: 20px !important; /* Space above the result */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
    }

    /* Error message with solid, vibrant color - IMPROVED */
    .stError > div { /* Target the inner div of st.error for background */
        background-color: #D32F2F !important; /* Deeper, solid red, fully opaque */
        color: white !important; /* White text for high contrast */
        font-size: 1.8em !important; /* Larger for emphasis */
        font-weight: bold !important; /* Bolder text */
        padding: 25px !important; /* More padding for prominence */
        border-radius: 8px !important;
        animation: fadeIn 1s !important;
        text-align: center !important; /* Centered for better visibility */
        margin-top: 20px !important; /* Space above the result */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
    }

    /* Warning message (text only, no box) - MINOR ADJUSTMENT */
    .stWarning {
        background-color: transparent !important; /* No background */
        color: #F9A825 !important; /* Amber text */
        font-size: 1.2em !important;
        padding: 10px 0 !important; /* Reduced vertical padding, no horizontal */
        border-radius: 0 !important;
        animation: fadeIn 1s !important;
        text-align: center !important; /* Center the warning text */
        font-weight: bold !important; /* Make warning bold */
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
            font-size: 1.4em !important; /* Adjusted for mobile */
        }
        .stTextArea textarea {
            height: 150px; /* Reduced for mobile */
        }
        .stButton button {
            padding: 10px 20px;
            font-size: 1em;
        }
        .stError > div, .stSuccess > div {
            font-size: 1.4em !important; /* Reduced for mobile */
            padding: 15px !important; /* Adjusted padding */
        }
        .stWarning {
            font-size: 1em !important; /* Reduced for mobile */
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
            # Ensure the input is transformed correctly based on your vectorsizer's expected input
            # If your vectorsizer expects a list of strings, this is correct.
            transform_input = vectorsizer.transform([inputn])
            prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("The News is Real!")
        else:
            st.error("The News is Fake!")
    else:
        # The warning will now appear as just text due to CSS changes
        st.warning("Please enter some text to analyze.")