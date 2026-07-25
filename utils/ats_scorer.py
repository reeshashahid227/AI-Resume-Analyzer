import re


def calculate_ats_score(resume_text):

    """
    Calculate ATS compatibility score using rule-based checks.
    Total score = 100
    """

    text = resume_text.lower()

    score = 0
    details = {}

    # 1. Contact Information - 15 points
    contact_score = 0

    if re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", text):
        contact_score += 8

    if re.search(r"\b(?:\+?\d[\d\s().-]{7,}\d)\b", text):
        contact_score += 7

    details["Contact Information"] = contact_score
    score += contact_score

    # 2. Important Sections - 25 points
    sections = {
        "Summary": [
            "summary",
            "professional summary",
            "profile",
            "objective"
        ],
        "Skills": [
            "skills",
            "technical skills",
            "core skills"
        ],
        "Experience": [
            "experience",
            "work experience",
            "professional experience"
        ],
        "Education": [
            "education",
            "academic background"
        ],
        "Projects": [
            "projects",
            "personal projects",
            "academic projects"
        ]
    }

    section_score = 0

    for section_name, keywords in sections.items():

        found = any(keyword in text for keyword in keywords)

        if found:
            section_score += 5

    section_score = min(section_score, 25)

    details["Resume Sections"] = section_score
    score += section_score

    # 3. Technical Skills - 25 points
    skills = [
        "python",
        "java",
        "c++",
        "javascript",
        "sql",
        "html",
        "css",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "git",
        "github",
        "streamlit",
        "django",
        "flask",
        "aws",
        "azure",
        "gcp",
        "tableau",
        "power bi",
        "spark",
        "hadoop",
        "mongodb",
        "postgresql",
        "mysql"
    ]

    matched_skills = []

    for skill in skills:

        if skill in text:
            matched_skills.append(skill)

    skill_score = min(len(matched_skills) * 2, 25)

    if len(matched_skills) >= 12:
        skill_score = 25

    details["Technical Skills"] = skill_score
    score += skill_score

    # 4. Experience - 15 points
    experience_score = 0

    if "experience" in text:
        experience_score += 10

    if re.search(r"\b(20\d{2})\s*[-–]\s*(20\d{2}|present)\b", text):
        experience_score += 5

    experience_score = min(experience_score, 15)

    details["Experience"] = experience_score
    score += experience_score

    # 5. Education - 10 points
    education_score = 0

    education_keywords = [
        "bachelor",
        "master",
        "bs",
        "bsc",
        "ms",
        "msc",
        "computer science",
        "software engineering",
        "university",
        "college"
    ]

    if any(keyword in text for keyword in education_keywords):
        education_score = 10

    details["Education"] = education_score
    score += education_score

    # 6. Keywords - 10 points
    keyword_score = 0

    keywords = [
    "machine learning",
    "data science",
    "data analysis",
    "artificial intelligence",
    "deep learning",
    "natural language processing",
    "data visualization",
    "statistics",
    "database",
    "analytics"
]

    matched_keywords = [
    keyword for keyword in keywords
    if keyword in text
]

    keyword_score = min(len(matched_keywords), 10)

    details["Keywords"] = keyword_score
    score += keyword_score

    # Final score
    score = min(score, 100)

    return {
        "ats_score": score,
        "details": details,
        "matched_skills": matched_skills
    }