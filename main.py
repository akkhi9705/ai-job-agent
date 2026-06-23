from app.search.greenhouse import search_jobs
from app.database.db import engine
from app.models.job import metadata
from sqlalchemy import insert
from app.models.job import jobs

metadata.create_all(engine)

print("Database Created")

data = search_jobs("stripe")

print(f"Jobs Found: {len(data['jobs'])}")

'''To Save Jobs to Database'''
with engine.begin() as conn:

    for job in data["jobs"]:

        conn.execute(
            insert(jobs).values(
                company="Stripe",
                title=job["title"],
                location=job["location"]["name"],
                apply_link=job["absolute_url"],
                source="Greenhouse"
            )
        )

print("Jobs Saved")