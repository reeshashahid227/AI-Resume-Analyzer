import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.text_preprocesser import clean_resume_text
from utils.ai_analyzer import analyze_resume, analyze_job_match
from utils.ats_scorer import calculate_ats_score


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>

    /* ================= MAIN APP ================= */

    .stApp {
        background-color: #f7f7f7;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ================= HEADER ================= */

    .main-title {
        font-size: 42px;
        font-weight: 750;
        color: #222222 !important;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #555555 !important;
        margin-bottom: 30px;
    }


    /* ================= SECTION TITLES ================= */

    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #222222 !important;
        margin-top: 32px;
        margin-bottom: 15px;
        border-left: 4px solid #333333;
        padding-left: 10px;
    }


    /* ================= ATS SCORE CARD ================= */

    .score-card {
        background-color: #ffffff !important;
        border: 1px solid #dddddd;
        border-radius: 14px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
    }

    .score-label {
        font-size: 16px;
        color: #555555 !important;
        margin-bottom: 5px;
    }

    .score-number {
        font-size: 44px;
        font-weight: 750;
        color: #222222 !important;
    }


    /* ================= CONTENT ================= */

    .content-card {
        background-color: #ffffff !important;
        color: #222222 !important;
        border: 1px solid #dddddd;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }


    /* ================= MARKDOWN TEXT ================= */

    .stMarkdown,
    .stMarkdown p,
    .stMarkdown li,
    .stMarkdown span,
    .stMarkdown strong {
        color: #222222;
    }


    /* ================= ATS METRICS ================= */

    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #dddddd;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    [data-testid="stMetricLabel"] {
        color: #555555 !important;
    }

    [data-testid="stMetricValue"] {
        color: #222222 !important;
        font-weight: 700;
    }


    /* ================= SKILLS ================= */

    .skill-box {
        background-color: #ffffff !important;
        border: 1px solid #dddddd;
        border-radius: 12px;
        padding: 18px;
        line-height: 1.8;
        color: #222222 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }


    /* ================= FILE UPLOADER ================= */

    [data-testid="stFileUploader"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 10px;
        border: 1px solid #dddddd;
    }


    /* ================= TEXT AREA ================= */

    textarea {
        border-radius: 10px !important;
    }


    /* ================= BUTTON ================= */

    .stButton > button {
        width: 100%;
        border-radius: 9px;
        border: 1px solid #222222;
        background-color: #222222;
        color: #ffffff !important;
        font-weight: 600;
        padding: 11px 20px;
    }

    .stButton > button:hover {
        background-color: #444444;
        border-color: #444444;
        color: #ffffff !important;
    }


    /* ================= PROGRESS BAR ================= */

    [data-testid="stProgress"] > div > div {
        background-color: #333333;
    }


    /* ================= WARNING ================= */

    [data-testid="stAlert"] {
        color: #222222 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">📄 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your resume, check ATS compatibility, and compare it with a job description.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- RESUME UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📤 Upload your Resume",
    type=["pdf"]
)


if uploaded_file is not None:

    try:

        # ---------------- STEP 1: EXTRACT TEXT ----------------

        resume_text = extract_text_from_pdf(uploaded_file)

        if not resume_text or not resume_text.strip():

            st.error("No readable text found in this PDF.")
            st.stop()


        # ---------------- STEP 2: CLEAN TEXT ----------------

        cleaned_text = clean_resume_text(resume_text)

        if not cleaned_text:

            st.error("Resume text could not be processed.")
            st.stop()


        # ---------------- STEP 3: ATS SCORING ----------------

        ats_result = calculate_ats_score(cleaned_text)

        st.markdown(
            '<div class="section-title">📊 ATS Compatibility</div>',
            unsafe_allow_html=True
        )

        score = ats_result["ats_score"]


        # ---------------- SCORE CARD ----------------

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:

            st.markdown(
                f'<div class="score-card">'
                f'<div class="score-label">'
                f'ATS Compatibility Score'
                f'</div>'
                f'<div class="score-number">'
                f'{score}/100'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

            st.progress(score / 100)


        # ---------------- STEP 4: AI ANALYSIS ----------------

        st.markdown(
            '<div class="section-title">🤖 AI Resume Analysis</div>',
            unsafe_allow_html=True
        )

        with st.spinner("AI is analyzing your resume..."):

            analysis = analyze_resume(
                cleaned_text,
                ats_result
            )


        # IMPORTANT:
        # Direct markdown rendering allows **bold**, headings,
        # bullets etc. to work correctly.

        st.markdown(
            '<div class="content-card">',
            unsafe_allow_html=True
        )

        st.markdown(analysis)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


        # ---------------- STEP 5: ATS DETAILS ----------------

        st.markdown(
            '<div class="section-title">📋 ATS Details</div>',
            unsafe_allow_html=True
        )

        details = ats_result["details"]

        columns = st.columns(len(details))

        for column, (category, points) in zip(
            columns,
            details.items()
        ):

            with column:

                st.metric(
                    label=category,
                    value=points
                )


        # ---------------- STEP 6: DETECTED SKILLS ----------------

        st.markdown(
            '<div class="section-title">🛠️ Detected Skills</div>',
            unsafe_allow_html=True
        )

        matched_skills = ats_result["matched_skills"]

        if matched_skills:

            skill_text = " • ".join(matched_skills)

            st.markdown(
                f'<div class="skill-box">'
                f'{skill_text}'
                f'</div>',
                unsafe_allow_html=True
            )

        else:

            st.write("No technical skills detected.")


        # ---------------- STEP 7: JOB MATCHING ----------------

        st.markdown(
            '<div class="section-title">'
            '💼 Job Description Matching'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(
            "Paste the job description below to compare it with your resume."
        )


        job_description = st.text_area(
            "📋 Job Description",
            height=250,
            placeholder="Paste the job description here...",
            key="job_description"
        )


        # ---------------- ANALYZE BUTTON ----------------

        if st.button("🎯 Analyze Job Match"):

            if not job_description.strip():

                st.warning(
                    "Please paste a job description first."
                )

            else:

                with st.spinner(
                    "Analyzing resume against job description..."
                ):

                    job_match_result = analyze_job_match(
                        cleaned_text,
                        job_description
                    )


                # ---------------- JOB MATCH RESULT ----------------

                st.markdown(
                    '<div class="section-title">'
                    '🎯 Job Match Analysis'
                    '</div>',
                    unsafe_allow_html=True
                )


                if job_match_result:

                    st.markdown(
                        '<div class="content-card">',
                        unsafe_allow_html=True
                    )

                    st.markdown(job_match_result)

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

                else:

                    st.write(
                        "Job match analysis could not be completed."
                    )


    except Exception as e:

        st.error(
            "Something went wrong while analyzing your resume."
        )

        st.info(
            "Please check your PDF and try again."
        )