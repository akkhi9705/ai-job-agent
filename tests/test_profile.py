from app.resume.loader import load_resumes
from app.resume.parser import (
    extract_resume_text,
    parse_resume_sections
)

from app.resume.profile import build_resume_profile

resumes = load_resumes()

for resume in resumes:

    text = extract_resume_text(resume)

    sections = parse_resume_sections(text)

    profile = build_resume_profile(
        resume,
        sections
    )

    print("=" * 80)

    print(profile)