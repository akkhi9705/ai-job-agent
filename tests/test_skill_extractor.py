from app.resume.loader import load_resumes
from app.resume.parser import (
    extract_resume_text,
    parse_resume_sections
)

from app.resume.profile import build_resume_profile
from app.resume.skill_extractor import extract_skills

resumes = load_resumes()

for resume in resumes:

    print("=" * 80)

    print(resume)

    text = extract_resume_text(resume)

    sections = parse_resume_sections(text)

    profile = build_resume_profile(
        resume,
        sections
    )

    skills = extract_skills(
        profile["skills"]
    )

    print("\nExtracted Skills:\n")

    for skill in skills:

        print(skill)