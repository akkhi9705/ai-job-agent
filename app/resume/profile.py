def build_resume_profile(file_name, sections):

    profile = {

        "resume_name": file_name,

        "summary": sections.get(
            "PROFESSIONAL SUMMARY",
            sections.get("SUMMARY", "")
        ),

        "skills": sections.get(
            "TECHNICAL SKILLS",
            sections.get("SKILLS", "")
        ),

        "experience": sections.get(
            "PROFESSIONAL EXPERIENCE",
            sections.get(
                "WORK EXPERIENCE",
                sections.get("EXPERIENCE", "")
            )
        ),

        "projects": sections.get(
            "PROJECTS",
            ""
        ),

        "education": sections.get(
            "EDUCATION",
            ""
        ),

        "certifications": sections.get(
            "CERTIFICATIONS",
            ""
        )

    }

    return profile