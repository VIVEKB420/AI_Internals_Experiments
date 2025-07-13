
import streamlit as st
from transformers import pipeline

st.title("LLM Summarizer")
text = st.text_area("Enter text to summarize:")

if text:
     summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
     summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
     st.subheader("Summary:")
     st.write(summary[0]['summary_text'])

