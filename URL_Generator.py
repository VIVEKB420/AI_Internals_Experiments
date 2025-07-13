
import streamlit as st
import urllib.parse

st.title("URL Generator")
base_url = st.text_input("Base URL", "https://example.com/search")
param = st.text_input("Query parameter (e.g. q)", "chatgpt")
if st.button("Generate URL"):
    full_url = f"{base_url}?q={urllib.parse.quote(param)}"
    st.write("Generated URL:", full_url)
