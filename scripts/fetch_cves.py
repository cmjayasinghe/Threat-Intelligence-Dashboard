import requests
import pandas as pd

print("Fetching CVEs...")

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

response = requests.get(url, timeout=30)

if response.status_code == 200:

    data = response.json()

    records = []

    for item in data["vulnerabilities"]:

        records.append({
            "CVE_ID": item["cve"]["id"]
        })

    df = pd.DataFrame(records)

    df.to_csv("data/cves.csv", index=False)

    print(f"Saved {len(df)} CVEs to data/cves.csv")

else:
    print("Failed to fetch CVEs")