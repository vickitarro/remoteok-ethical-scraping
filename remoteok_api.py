import requests
import pandas as pd

# RemoteOK public API
url = "https://remoteok.com/api"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)

jobs_json = response.json()

# First item is metadata → skip it
jobs = jobs_json[1:]

data = []

for job in jobs:
    title = job.get("position")
    company = job.get("company")
    location = job.get("location")

    if title and company:
        data.append({
            "job_title": title,
            "company": company,
            "location": location
        })

df = pd.DataFrame(data)

print(df.head())
print("Total jobs extracted:", len(df))
df.to_csv("remoteok_jobs.csv", index=False)
print("Saved to remoteok_jobs.csv")
