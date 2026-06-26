from app.resume.loader import load_resumes
from app.resume.parser import (
    extract_resume_text,
    parse_resume_sections
)

resumes = load_resumes()

for resume in resumes:

    print("=" * 80)

    print(resume)

    text = extract_resume_text(resume)

    sections = parse_resume_sections(text)

    print("\nSections Found:\n")

    print("\nTechnical Skills:\n")

    print(
        sections.get(
            "TECHNICAL SKILLS",
             "Not Found"
        )
    )