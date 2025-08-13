import streamlit as st
import joblib

# Load the vectorsizer and model
vectorsizer = joblib.load("vectorsizer.jb")
model = joblib.load("lr_model.jb")

# Custom CSS and HTML for newspaper theme
st.markdown(
    """
    <style>
    /* Newspaper background */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #2E2E2E; /* Dark gray text for readability */
    }

    /* Container for content */
    .content {
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white overlay */
        padding: 20px;
        border: 2px solid #D3D3D3; /* Light gray border */
        border-radius: 10px;
        margin: 20px auto;
        max-width: 800px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Georgia', serif; /* Classic newspaper font */
    }

    /* Title styling */
    h1 {
        font-size: 2.5em;
        color: #1A237E; /* Dark blue for header */
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid #1A237E;
        padding-bottom: 10px;
    }

    /* Text area and button */
    .stTextArea, .stButton {
        margin: 10px 0;
    }
    .stButton button {
        background-color: #1A237E;
        color: white;
        padding: 50px 20px;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        transition: transform 0.3s, background-color 0.3s;
    }
    .stButton button:hover {
        transform: scale(1.05);
        background-color: #0D47A1;
    }

    /* Success and error messages */
    .stSuccess, .stError {
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
        transform_input = vectorsizer.transform([inputn])
        prediction = model.predict(transform_input)

        with st.spinner("Analyzing..."):  # Spinner animation while processing
            st.markdown('<div class="content">', unsafe_allow_html=True)
            if prediction[0] == 1:
                st.success("The News is Real! ")
            else:
                st.error("The News is Fake! ")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to Analyze. ")