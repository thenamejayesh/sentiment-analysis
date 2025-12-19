import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="centered"
)

# Load sentiment model (cached)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# Simple CSS (safe version)
st.markdown(
    "<style>"
    "body {background-color: #f4f6f9;}"
    ".title {text-align: center; font-size: 34px; font-weight: bold; color: #2c3e50;}"
    ".subtitle {text-align: center; font-size: 18px; color: #555;}"
    ".box {padding:15px; border-radius:10px; background:#ffffff; "
    "box-shadow: 0px 4px 8px rgba(0,0,0,0.1); text-align:center; font-size:20px;}"
    "</style>",
    unsafe_allow_html=True
)

# Title
st.markdown("<div class='title'>Sentiment Analysis App</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Check if text is Positive or Negative</div>", unsafe_allow_html=True)

st.write("")

# Input
text = st.text_area(
    "✍️ Enter text:",
    placeholder="Example: I don't like this product",
    height=120
)

# Button
if st.button("🔍 Analyze Sentiment"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        result = model(text)[0]
        label = result["label"]
        score = round(result["score"] * 100, 2)

        if label == "POSITIVE":
            st.markdown(
                f"<div class='box'>😊 <b>Positive Sentiment</b><br>Confidence: {score}%</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='box'>😞 <b>Negative Sentiment</b><br>Confidence: {score}%</div>",
                unsafe_allow_html=True
            )

st.write("")
st.markdown("<center>Built with ❤️ using Streamlit & Transformers</center>", unsafe_allow_html=True)

