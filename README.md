# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Python, Streamlit, Groq AI, and rule-based ATS scoring**.

The application analyzes a resume from a PDF, extracts and cleans the resume text, calculates an ATS compatibility score, provides AI-powered resume feedback, detects technical skills, and compares the resume against a job description.

---

## 🚀 Features

### 📄 Resume PDF Upload
Upload a resume in PDF format directly through the Streamlit interface.

### 🔍 PDF Text Extraction
The application extracts readable text from the uploaded resume using `pypdf`.

### 🧹 Resume Text Preprocessing
Extracted resume text is cleaned and normalized before analysis to improve consistency.

### 📊 ATS Compatibility Score
The application calculates an ATS score out of 100 using rule-based checks such as:

- Contact Information
- Resume Sections
- Technical Skills
- Experience
- Education
- Keywords

### 🤖 AI Resume Analysis
Groq AI analyzes the resume and provides:

- Professional Summary
- Strengths
- Weaknesses
- Missing Skills
- ATS-Based Improvement Suggestions

### 🛠️ Technical Skill Detection
The system identifies technical skills found in the resume.

### 💼 Job Description Matching
Paste a job description and compare it with the uploaded resume.

The job matching analysis provides:

- Job Match Score
- Matched Skills
- Missing Skills
- Matched Keywords
- Missing Keywords
- Job Match Strengths
- Job Match Weaknesses
- Job-Specific Improvement Suggestions

### 🎨 Professional Streamlit UI
The application includes:

- Clean dashboard layout
- ATS score card
- Progress bar
- AI analysis section
- ATS detail metrics
- Detected skills section
- Job description matching section
- Loading indicators
- Error handling

---

## 🔄 How It Works

```text
Upload Resume PDF
        ↓
Extract Resume Text
        ↓
Clean & Preprocess Text
        ↓
Calculate ATS Score
        ↓
Detect Technical Skills
        ↓
Send Resume to Groq AI
        ↓
Generate AI Resume Analysis
        ↓
Paste Job Description
        ↓
Compare Resume with Job Description
        ↓
Generate Job Match Analysis
```

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| pypdf | PDF text extraction |
| Groq | AI-powered resume and job analysis |
| python-dotenv | Environment variable management |
| Regular Expressions | Text preprocessing and cleaning |

---

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
└── utils/
    ├── __init__.py
    ├── pdf_reader.py
    ├── text_preprocesser.py
    ├── ai_analyzer.py
    └── ats_scorer.py
```

> Your exact project structure may vary slightly depending on the files you have added.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd AI-Resume-Analyzer
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 📦 Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

## 🔐 Groq API Key Setup

The AI analysis uses a Groq API key.

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Do **not** upload your `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 How to Test

### Test 1 — Resume Analysis

1. Upload a PDF resume.
2. Check whether the text is extracted successfully.
3. Verify the ATS score.
4. Review the AI analysis.
5. Check detected technical skills.

### Test 2 — Job Matching

1. Upload a resume.
2. Paste a Data Scientist job description.
3. Click **Analyze Job Match**.
4. Check:
   - Job Match Score
   - Matched Skills
   - Missing Skills
   - Matched Keywords
   - Missing Keywords
   - Job-specific suggestions

### Test 3 — Invalid PDF

Try a PDF with no readable text and verify that the application displays an appropriate error message.

---

## 📊 Example Output

### ATS Compatibility

```text
ATS Compatibility Score: 76/100
```

### Detected Skills

```text
Python
SQL
Pandas
NumPy
Scikit-learn
Git
Flask
AWS
Tableau
MySQL
```

### Job Match

```text
Job Match Score: 85/100
```

The AI then identifies matched skills, missing skills, keywords, strengths, weaknesses, and improvement suggestions.

---

## 🎯 Project Goals

The main goal of this project is to help job seekers understand how well their resume is optimized for ATS systems and how closely it matches a specific job description.

Instead of manually reviewing every requirement, the application combines:

**Rule-Based ATS Scoring + AI Resume Analysis + Job Matching**

to provide actionable resume feedback.

---

## 🔮 Future Improvements

Potential future features include:

- 📥 Downloadable resume analysis report
- 📄 Resume improvement suggestions with rewritten sections
- 🎯 More advanced job-description keyword matching
- 📈 Visual ATS score dashboard
- 🧠 Semantic similarity using embeddings
- 📝 AI-generated professional summary
- ✨ AI-powered resume rewriting
- 📊 Resume vs. job description comparison charts
- 🔐 User authentication
- 🌐 Production deployment
- 📱 Improved mobile responsiveness

---




