import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
    search_term="software engineer intern",
    google_search_term="software engineer intern jobs near Toronto, Ontario since yesterday",
    # Glassdoor's location API rejects province abbreviations; provide the full
    # region and country to avoid a 400 "location not parsed" response.
    location="Toronto, Ontario, Canada",
    job_type="internship",
    results_wanted=20,
    hours_old=24,
    # Explicitly pass the country so Indeed/Glassdoor map to the correct domains
    # (e.g. glassdoor.ca) and ZipRecruiter recognises the search region.
    country_indeed="Canada",
)
print(f"Found {len(jobs)} jobs")
jobs.to_csv("job1.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
