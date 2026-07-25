import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(resume_text, ats_result):

    prompt = f"""
You are an expert HR recruiter.

Analyze the following resume and provide improvement
suggestions based on its ATS results.

IMPORTANT RULES:
- Do NOT calculate or change the ATS score.
- Treat the provided ATS score as the final score.
- Do NOT invent skills, experience, education, certifications, or achievements.
- If something is not present in the resume, clearly say it is missing.
- Base your analysis on the actual resume and ATS results.
- Do not give another overall resume score.
- Interpret each ATS component according to its maximum score.
- Do not call a component weak or low when it has received full marks.


IMPORTANT ATS SCORING RULES:
- Contact Information maximum = 15
- Resume Sections maximum = 25
- Technical Skills maximum = 25
- Experience maximum = 15
- Education maximum = 10
- Keywords maximum = 10
- Always display each score using its correct maximum.
- Never change, recalculate, or invent ATS scores.
- Do not describe a full-score category as weak or low.

Resume:
{resume_text}

ATS Score:
{ats_result["ats_score"]}/100

ATS Details:
{ats_result["details"]}

Detected Technical Skills:
{ats_result["matched_skills"]}

Provide:

1. Professional Summary

2. Strengths

3. Weaknesses

4. Missing Skills

5. ATS-Based Improvement Suggestions


"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def analyze_job_match(resume_text, job_description):

    prompt = f"""
You are an expert ATS and recruitment analyst.

Compare the resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the match and provide:

1. Job Match Score (0-100)
2. Matched Skills
3. Missing Skills
4. Matched Keywords
5. Missing Keywords
6. Job Match Strengths
7. Job Match Weaknesses
8. Job-Specific Improvement Suggestions

IMPORTANT:
- Do not invent skills or experience.
- Only consider skills actually present in the resume as matched.
- Clearly separate missing skills from existing skills.
- The Job Match Score is different from the ATS Score.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content