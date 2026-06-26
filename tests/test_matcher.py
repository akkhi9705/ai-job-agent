from app.resume.loader import load_resumes
from app.resume.parser import (
    extract_resume_text,
    parse_resume_sections
)
from app.resume.profile import build_resume_profile
from app.resume.skill_extractor import extract_skills

from app.search.greenhouse import search_jobs
from app.search.jd_extractor import extract_jd

from app.jd.parser import extract_jd_text
from app.jd.skill_extractor import extract_jd_skills

from app.resume.matcher import calculate_score
from app.filter.role_filter import is_cs_role

# ----------------------------
# Find first CS job
# ----------------------------

jobs = search_jobs("stripe")

selected_job = None

for job in jobs["jobs"]:

    if is_cs_role(job["title"]):
        selected_job = job
        break

if selected_job is None:
    print("No CS Job Found")
    exit()

print("=" * 80)
print("JOB")
print(selected_job["title"])

jd = extract_jd(
    selected_job["absolute_url"]
)

jd_text = extract_jd_text(jd)

jd_skills = extract_jd_skills(jd_text)

print("\nJD Skills")

print(jd_skills)

print("\n" + "=" * 80)

# ----------------------------
# Score every resume
# ----------------------------

resumes = load_resumes()

best_resume = None
best_score = 0

for resume in resumes:

    text = extract_resume_text(resume)

    sections = parse_resume_sections(text)

    profile = build_resume_profile(
        resume,
        sections
    )

    resume_skills = extract_skills(
        profile["skills"]
    )

    result = calculate_score(
        resume_skills,
        jd_skills
    )

    print(resume)

    print("Score:", result["score"])

    print("Matched:", result["matched"])

    print("Missing:", result["missing"])

    print()

    if result["score"] > best_score:

        best_score = result["score"]

        best_resume = resume

print("=" * 80)

print("BEST RESUME")

print(best_resume)

print("SCORE")

print(best_score)