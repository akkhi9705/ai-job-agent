from sqlalchemy import insert

from app.search.greenhouse import search_jobs
from app.search.jd_extractor import extract_jd

from app.database.db import engine
from app.models.job import metadata
from app.models.job import jobs

from app.filter.sponsorship import detect_sponsorship
from app.filter.role_filter import is_cs_role
from app.filter.location_filter import is_us_job

# Create tables
metadata.create_all(engine)

# Fetch jobs
data = search_jobs("stripe")

print(f"Jobs Found: {len(data['jobs'])}")

# Process first 50 jobs
for job in data["jobs"][:100]:

    print("\n--------------------------------")
    print("Processing:", job["title"])

    # Extract JD
    jd = extract_jd(
        job["absolute_url"]
    )

    # Sponsorship Check
    sponsorship_status = detect_sponsorship(jd)

    print(
        f"Sponsorship Status: {sponsorship_status}"
    )

    # CS Role Check
    cs_role = is_cs_role(
        job["title"]
    )

    print(
        f"CS Role: {cs_role}"
    )

    # US Location Check
    us_job = is_us_job(
        job["location"]["name"]
    )

    print(
        f"US Job: {us_job}"
    )

    # Save only relevant jobs
    if (
        cs_role
        and us_job
        and sponsorship_status != "NO_SPONSORSHIP"
    ):

        print("✅ Saving Job")

        with engine.begin() as conn:

            conn.execute(
                insert(jobs).values(
                    company="Stripe",
                    title=job["title"],
                    location=job["location"]["name"],
                    jd=jd,
                    sponsorship_status=sponsorship_status,
                    is_cs_role=str(cs_role),
                    is_us_job=str(us_job),
                    apply_link=job["absolute_url"],
                    source="Greenhouse"
                )
            )

    else:

        print("❌ Skipped")

print("\nAll jobs processed successfully!")