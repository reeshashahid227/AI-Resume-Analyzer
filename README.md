# 📄 AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM%20API-orange)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-powered Resume Analyzer built with **Python, Streamlit, Groq AI, and rule-based ATS scoring**.

The application analyzes a resume from a PDF, extracts and cleans the resume text, calculates an ATS compatibility score, provides AI-powered resume feedback, detects technical skills, and compares the resume against a job description.

---

## 🚀 Live Demo

👉 **[Try it here](https://ai-resume-analyzer-bxcexukxwsakw4qqi3nlmn.streamlit.app)**

Upload any PDF resume and get an instant ATS score, AI-powered feedback, and job description matching — no setup required.



## 🚀 Features

### 📄 Resume PDF Upload
Upload a resume in PDF format directly through the Streamlit interface.

### 🔍 PDF Text Extraction
The application extracts readable text from the uploaded resume using `PyMuPDF`.

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
Groq AI (Llama 3.3 70B) analyzes the resume and provides:

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

```
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

| Technology          | Purpose                            |
| ------------------- | ----------------------------------- |
| Python              | Core programming language          |
| Streamlit           | Web application interface          |
| PyMuPDF             | PDF text extraction                |
| Groq                | AI-powered resume and job analysis |
| python-dotenv       | Environment variable management    |
| Regular Expressions | Text preprocessing and cleaning    |

---

## 📁 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── screenshots/
│   ├── 01_upload.png
│   ├── 02_ats_score.png
│   ├── 03_ai_analysis.png
│   ├── 04_skills_jobmatch.png
│   ├── 05_job_description.png
│   └── 06_job_match_result.png
│
└── utils/
    ├── __init__.py
    ├── pdf_reader.py
    ├── text_preprocesser.py
    ├── ai_analyzer.py
    └── ats_scorer.py
```

---

## ⚙️ Installation (Run Locally)

### 1. Clone the repository
```
git clone https://github.com/reeshashahid227/AI-Resume-Analyzer.git
```

### 2. Open the project folder
```
cd AI-Resume-Analyzer
```

### 3. Create a virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Set up your Groq API key
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 6. Run the application
```
streamlit run app.py
```

---

## 📊 Example Output

### ATS Compatibility
```
ATS Compatibility Score: 76/100
```

### Detected Skills
```
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
```
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

- 📥 Downloadable resume analysis report (PDF export)
- 📄 Resume improvement suggestions with rewritten sections
- 🎯 More advanced job-description keyword matching
- 📈 Visual ATS score dashboard
- 🧠 Semantic similarity using embeddings
- 📝 AI-generated professional summary
- ✨ AI-powered resume rewriting
- 📊 Resume vs. job description comparison charts
- 🔐 User authentication
- 📱 Improved mobile responsiveness

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
