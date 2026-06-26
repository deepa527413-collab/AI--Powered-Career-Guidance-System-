# ai_engine.py

career_data = {
    "python": {
        "career": "AI Engineer",
        "skills": [
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch"
        ],
        "courses": [
            "Python Programming",
            "Machine Learning",
            "Deep Learning Specialization"
        ]
    },

    "java": {
        "career": "Java Developer",
        "skills": [
            "Spring Boot",
            "Hibernate",
            "REST API"
        ],
        "courses": [
            "Core Java",
            "Advanced Java",
            "Spring Boot"
        ]
    },

    "html": {
        "career": "Frontend Developer",
        "skills": [
            "CSS",
            "JavaScript",
            "Bootstrap",
            "React"
        ],
        "courses": [
            "HTML & CSS",
            "JavaScript",
            "React JS"
        ]
    },

    "sql": {
        "career": "Database Administrator",
        "skills": [
            "MySQL",
            "PostgreSQL",
            "Database Design"
        ],
        "courses": [
            "SQL",
            "Database Management",
            "Oracle DBA"
        ]
    }
}


def recommend_career(user_skills):
    user_skills = user_skills.lower()

    for skill in career_data:
        if skill in user_skills:
            return career_data[skill]

    return {
        "career": "Software Engineer",
        "skills": [
            "Problem Solving",
            "Programming",
            "Communication"
        ],
        "courses": [
            "Data Structures",
            "Algorithms",
            "Programming Fundamentals"
        ]
    }
