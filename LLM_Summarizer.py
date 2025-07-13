
import streamlit as st

def summarize(text):
    return text[:100] + "..."

st.title("LLM Summarizer")
text_input = st.text_area("Enter text to summarize")
if st.button("Summarize"):
    st.write(summarize(text_input))
