import re


def extract_skills(skill_text):

    skills = []

    # Split the text into lines
    lines = skill_text.split("\n")

    for line in lines:

        # Ignore empty lines
        if not line.strip():
            continue

        # Remove category names like Programming :
        if ":" in line:
            line = line.split(":", 1)[1]

        # Split by commas
        parts = line.split(",")

        for part in parts:

            skill = part.strip().lower()

            # Remove periods
            skill = skill.replace(".", "")

            if skill:
                skills.append(skill)

    # Remove duplicates

    unique_skills = []

    for skill in skills:

        if skill not in unique_skills:
            unique_skills.append(skill)

    return unique_skills