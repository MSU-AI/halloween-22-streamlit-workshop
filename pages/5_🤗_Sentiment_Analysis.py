import streamlit as st
from transformers import pipeline

st.title("Sentiment Analysis")

st.write("Enter some text and I will determine its sentiment (positive or negative) using the Hugging Face transformers library.")
text = st.text_input(label="Enter some text")

sentiment_pipeline = pipeline("sentiment-analysis")
result = sentiment_pipeline(text)
st.write(result)