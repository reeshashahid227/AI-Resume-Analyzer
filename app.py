import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.text_preprocesser import clean_resume_text
from utils.ai_analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume for analysis.")

uploaded_file = st.file_uploader(
    "Choose a Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    text = extract_text_from_pdf(uploaded_file)
    clean_text=clean_resume_text(text)
    AI_response=analyze_resume(clean_text)
    st.success("Resume uploaded successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "AI Resume Analysis",
        AI_response,
        height=400
    )