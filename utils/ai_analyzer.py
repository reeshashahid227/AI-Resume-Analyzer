import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume(resume_text):

    prompt = f"""
You are an expert HR recruiter.

Analyze the following resume.

Resume:
{resume_text}

Provide:

1. Professional Summary

2. Strengths

3. Weaknesses

4. Missing Skills

5. Improvement Suggestions
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