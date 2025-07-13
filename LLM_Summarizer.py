import streamlit as st
from transformers import pipeline

"""
Pre-requisites to run this app:
1) Make sure the relevant libraries like 'Streamlit' and 'yngrok' are installed.
2) You have signed up for ngrok and received the auth token.
2) Press Control + Enter after providing the text in the box to summarize .

"""

st.title("LLM Summarizer")
text = st.text_area("Enter text to summarize:")


"""Example text =
Despite the fact that piranhas are relatively harmless, many people continue to believe the pervasive myth that piranhas are dangerous to humans. This impression of piranhas is exacerbated by their mischaracterization in popular media. For example, the promotional poster for the 1978 horror film Piranha features an oversized piranha poised to bite the leg of an unsuspecting woman. Such a terrifying representation easily captures the imagination and promotes unnecessary fear. While the trope of the man-eating piranhas lends excitement to the adventure stories, it bears little resemblance to the real-life piranha. By paying more attention to fact than fiction, humans may finally be able to let go of this inaccurate belief..
"""
if text:
     summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
     summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
     st.subheader("Summary:")
     st.write(summary[0]['summary_text'])


with open("LLM_Summarizer.py", "w") as f:
    f.write(code)


"""Notes
1) Inference means process of generating outputs (predictions, tokens, or text) from a trained Large Language Model (LLM) like GPT, LLaMA, or Mistral.
2) It works in stages. First the input is converted into tokens.
3) These tokens are passed through a embedding layer to get the contexual meaning and relationships betwenn them. These are vectors.
4) These vectors go through the LLM Stack(Self Attention, FeedForward layers, Layer Normalization). Self Attention focuses on important parts of the input. FF layers transforms and learns new representations. Normalization for stability and depth.
5) Output is the logits. These are predicted vector of tokens. Raw scores for each possible next token in vocab.
6) Finally, the decoding happens. The logits are converted into probabilities and model decides the next token using different algos like Greedy decoding(most probable toekn), sampling(pick random from top k), Beam Search(explore multiple token paths and select best one)
"""
