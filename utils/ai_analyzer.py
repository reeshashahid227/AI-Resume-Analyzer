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

6. Overall Resume Score (out of 100)
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