import csv
from jobspy import scrape_jobs
import openpyxl
import os

jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="sql",
    google_search_term="SQL or Data Engineer jobs near San Francisco, CA since yesterday",
    location="San Francisco, CA",
    results_wanted=20,
    hours_old=72,
    country_indeed='USA',
    
    #linkedin_fetch_description=True, # gets more info such as description, direct job url (slower)
    #proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
file_path = "jobs.xlsx"

# Check if the file exists
if os.path.exists(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
else:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    # Write the header if the file is new
    header = list(jobs.columns)
    sheet.append(header)

# Find the next empty row
next_row = sheet.max_row + 1

# Write the job data
for index, row in jobs.iterrows():
    for col_num, value in enumerate(row, start=1):
        sheet.cell(row=next_row, column=col_num, value=value)
    next_row += 1

# Save the workbook
workbook.save(file_path)
