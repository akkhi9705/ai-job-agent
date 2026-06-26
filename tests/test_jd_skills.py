from app.search.greenhouse import search_jobs
from app.search.jd_extractor import extract_jd

from app.jd.parser import extract_jd_text
from app.jd.skill_extractor import extract_jd_skills


jobs = search_jobs("stripe")

from app.filter.role_filter import is_cs_role

job = None

for j in jobs["jobs"]:

    if is_cs_role(j["title"]):
        job = j
        break

if job is None:
    print("No CS job found.")
    exit()

print(job["title"])

jd = extract_jd(
    job["absolute_url"]
)

text = extract_jd_text(jd)

skills = extract_jd_skills(text)

print("\nJD Skills\n")

for skill in skills:

    print(skill)