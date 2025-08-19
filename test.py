import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
    search_term="software engineer intern",
    google_search_term="software engineer intern jobs near Toronto, ON since yesterday",
    location="Toronto, ON",
    job_type="internship",
    results_wanted=20,
    hours_old=24,
    country_indeed="canada",
)
print(f"Found {len(jobs)} jobs")
jobs.to_csv("job1.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
