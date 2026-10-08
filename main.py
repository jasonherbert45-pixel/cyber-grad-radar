from database import create_database, add_job, get_jobs


create_database()

add_job(
    "Example Security Ltd",
    "Graduate Cyber Security Engineer",
    "London",
    "https://example.com/job/123",
    "2026-10-08"
)

jobs = get_jobs()

for job in jobs:
    print(job)

print("Cyber Grad Radar database ready.")