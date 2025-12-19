import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="centered"
)

# Load model (cached for performance)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# Custom CSS for attractive UI
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        color: #2c3e50;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 18px;
    }
    .result-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1)
