import streamlit as st
import joblib

# Load the vectorizer and model
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

    /* Text area styling */
    .stTextArea textarea {
        width: 100%;
        height: 200px; /* Increased height for larger text box */
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
        padding: 12px 25px; /* Larger padding for prominence */
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        transition: transform 0.3s, background-color 0.3s;
    }
    .stButton button:hover {
        transform: scale(1.05);
        background-color: #5D4037; /* Darker shade on hover */
    }

    /* Success and error messages */
    .stSuccess {
        background-color: #E8F5E9; /* Light green for success */
        color: #2E7D32; /* Dark green text */
        font-size: 1.2em;
        padding: 10px;
        border-radius: 5px;
        animation: fadeIn 1s;
    }
    .stError {
        background-color: #FFEBEE; /* Light red for error */
        color: #C62828; /* Dark red text */
        font-size: 1.2em;
        padding: 10px;
        border-radius: 5px;
        animation: fadeIn 1s;
    }

    /* Warning message */
    .stWarning {
        background-color: #FFFDE7; /* Light yellow */
        color: #F9A825; /* Amber text */
        font-size: 1.2em;
        padding: 10px;
        border-radius: 5px;
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
        .stTextArea textarea {
            height: 150px; /* Slightly reduced for mobile */
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
        st.markdown('<div class="content">', unsafe_allow_html=True)
        if prediction[0] == 1:
            st.success("The News is Real! ")
        else:
            st.error("The News is Fake! ")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to Analyze. ")