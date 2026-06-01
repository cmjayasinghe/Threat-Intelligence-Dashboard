import requests
import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

url = "https://api.abuseipdb.com/api/v2/blacklist"

headers = {
    "Accept": "application/json",
    "Key": API_KEY
}

params = {
    "confidenceMinimum": 90
}

print("Fetching malicious IPs...")

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=30
)

if response.status_code == 200:

    data = response.json()

    records = []

    for ip in data["data"]:

        records.append({
            "ipAddress": ip["ipAddress"],
            "abuseConfidenceScore": ip["abuseConfidenceScore"],
            "countryCode": ip["countryCode"]
        })

    df = pd.DataFrame(records)

    df.to_csv(
        "data/malicious_ips.csv",
        index=False
    )

    print(f"Saved {len(df)} malicious IPs")

else:

    print("API Error")
    print(response.status_code)
    print(response.text)