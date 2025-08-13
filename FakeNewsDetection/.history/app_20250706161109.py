import streamlit as st
import joblib

# Load the vectorsizer and model
vectorsizer = joblib.load("vectorsizer.jb")
model = joblib.load("lr_model.jb")

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
        font-size: 1.5em; /* Larger and more visible */
        color: #4A2C2A; /* Match title color */
        font-weight: bold; /* Bolder text */
        margin-bottom: 5px;
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
    }
    .stButton button:hover {
        transform: scale(1.05);
        background-color: #5D4037; /* Darker shade on hover */
    }

    /* Success message with solid color */
    .stSuccess {
        background-color: #6D4C41; /* Warm brown button */
        color: white; /* White text */
        font-size: 1.3em; /* Slightly larger */
        padding: 15px; /* More padding */
        border-radius: 5px;
        animation: fadeIn 1s;
        border: none; /* Remove any border */
    }

    /* Error message with solid, vibrant color */
    .stError {
        background-color: #D32F2F; /* Deeper, solid red */
        color: black; /* black text for high contrast */
        font-size: 1.5em; /* Larger for emphasis */
        font-weight: bold; /* Bolder text */
        padding: 20px; /* More padding for prominence */
        border-radius: 5px;
        animation: fadeIn 1s;
        border: none; /* Remove any border */
        text-align: center; /* Centered for better visibility */
    }

    /* Warning message (text only, no box) */
    .stWarning {
        background-color: transparent; /* No background */
        color: #F9A825; /* Amber text */
        font-size: 1.2em;
        padding: 10px;
        border-radius: 0;
        animation: fadeIn 1s;
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
            font-size: 1.2em; /* Reduced for mobile */
        }
        .stTextArea textarea {
            height: 150px; /* Reduced for mobile */
        }
        .stError {
            font-size: 1.2em; /* Reduced for mobile */
            padding: 15px; /* Adjusted padding */
        }
    }
    </style>
    <div class="content">
        <h1>Fake News Detector</h1>
        <p style="text-align: center; font-style: italic;">Enter a News Article below to check its authenticity.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# App content
inputn = st.text_area("News Article:", "")

if st.button("Check News"):
    if inputn.strip():
        with st.spinner("Analyzing..."):
            transform_input = vectorsizer.transform([inputn])
            prediction = model.predict(transform_input)
        if prediction[0] == 1:
            st.success("The News is Real! ")
        else:
            st.error("The News is Fake! ")
    else:
        st.warning("Please enter some text to Analyze. ")