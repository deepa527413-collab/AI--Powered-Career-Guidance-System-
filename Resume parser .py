# resume_parser.py

import os
import PyPDF2

# List of skills to detect
SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "bootstrap",
    "react",
    "angular",
    "node",
    "flask",
    "django",
    "sql",
    "mysql",
    "mongodb",
    "machine learning",
    "deep learning",
    "data science",
    "artificial intelligence",
    "power bi",
    "excel",
    "git"
]


def extract_text(pdf_path):
    """Extract text from a PDF file."""
    text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.lower()


def extract_skills(text):
    """Return matching skills found in the resume."""
    found = []

    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill.title())

    return sorted(list(set(found)))


def recommend_career(skills):

    skills = [s.lower() for s in skills]

    if "python" in skills and "machine learning" in skills:
        return "AI Engineer"

    if "python" in skills and "data science" in skills:
        return "Data Scientist"

    if "html" in skills and "css" in skills and "javascript" in skills:
        return "Frontend Developer"

    if "flask" in skills or "django" in skills:
        return "Backend Developer"

    if "react" in skills and "node" in skills:
        return "Full Stack Developer"

    if "mysql" in skills or "sql" in skills:
        return "Database Administrator"

    return "Software Engineer"


def analyze_resume(pdf_path):
    text = extract_text(pdf_path)

    skills = extract_skills(text)

    career = recommend_career(skills)

    return {
        "skills": skills,
        "career": career
    }
