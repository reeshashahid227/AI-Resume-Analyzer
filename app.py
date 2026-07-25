import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.text_preprocesser import clean_resume_text
from utils.ai_analyzer import analyze_resume
from utils.ats_scorer import calculate_ats_score


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume for AI-powered analysis and ATS scoring.")


uploaded_file = st.file_uploader(
    "Choose a Resume (PDF)",
    type=["pdf"]
)


if uploaded_file is not None:

    # Step 1: Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Step 2: Clean text
    cleaned_text = clean_resume_text(resume_text)

    # Step 3: AI Analysis
    st.subheader("🤖 AI Resume Analysis")

    analysis = analyze_resume(cleaned_text)

    st.write(analysis)

    # Step 4: ATS Scoring
    ats_result = calculate_ats_score(cleaned_text)

    st.subheader("📊 ATS Score")

    st.metric(
        "ATS Compatibility",
        f"{ats_result['ats_score']}/100"
    )

    # Step 5: ATS Details
    st.subheader("📋 ATS Details")

    for category, points in ats_result["details"].items():
        st.write(f"**{category}:** {points}")

    # Step 6: Detected Skills
    st.subheader("🛠️ Detected Skills")

    if ats_result["matched_skills"]:
        st.write(", ".join(ats_result["matched_skills"]))
    else:
        st.write("No technical skills detected.")