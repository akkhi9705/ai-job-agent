from sqlalchemy import insert

from app.search.greenhouse import search_jobs
from app.search.jd_extractor import extract_jd

from app.database.db import engine
from app.models.job import metadata
from app.models.job import jobs

metadata.create_all(engine)

data = search_jobs("stripe")

for job in data["jobs"][:5]:

    print("Processing:", job["title"])

    jd = extract_jd(
        job["absolute_url"]
    )

    with engine.begin() as conn:

        conn.execute(
            insert(jobs).values(
                company="Stripe",
                title=job["title"],
                location=job["location"]["name"],
                jd=jd,
                apply_link=job["absolute_url"],
                source="Greenhouse"
            )
        )

print("Done")