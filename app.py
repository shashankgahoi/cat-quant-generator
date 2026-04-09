import streamlit as st
from generator import generate_question

st.set_page_config(page_title="CAT Quant Generator", layout="centered")

st.title("📘 CAT Quant Paper Generator")

topic = st.selectbox(
    "Select Topic",
    ["Arithmetic", "Algebra", "Geometry", "Number System", "Modern Math"]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate Question"):
    with st.spinner("Generating..."):
        question = generate_question(topic, difficulty)
        st.text_area("Question Output", question, height=300)
