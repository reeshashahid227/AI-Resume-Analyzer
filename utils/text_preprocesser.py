import re

def clean_resume_text(text):

    text=text.strip()
    text=re.sub(r'[ ]+'," ",text)
    text=re.sub(r'\t'," ",text)
    text=re.sub(r'\n\s*\n+'," ",text)
    text = re.sub(r"-{2,}", "-", text)
    text = re.sub(r"[★☆✓✔✦✪]", "", text)
    text = re.sub(r"[\u2022\u25CF\u25BA\u25AA]", "", text)

    return text

