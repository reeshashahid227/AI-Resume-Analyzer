import streamlit as st
from utils.pdf_reader import extract_text_from_pdf

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

    st.success("Resume uploaded successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        text,
        height=400
    )