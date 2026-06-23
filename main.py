from app.search.greenhouse import search_jobs

data = search_jobs("stripe")

print(f"Jobs Found: {len(data['jobs'])}")