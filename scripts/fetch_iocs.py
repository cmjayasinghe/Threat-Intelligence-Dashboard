import requests
import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OTX_API_KEY")

headers = {
    "X-OTX-API-KEY": API_KEY
}

url = "https://otx.alienvault.com/api/v1/pulses/subscribed"

print("Connecting to OTX...")

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("Status Code:", response.status_code)

if response.status_code == 200:

    data = response.json()

    records = []

    for pulse in data.get("results", []):

        records.append({
            "pulse_name": pulse.get("name"),
            "author": pulse.get("author_name"),
            "created": pulse.get("created"),
            "indicator_count": pulse.get("indicator_count")
        })

    df = pd.DataFrame(records)

    df.to_csv(
        "data/iocs.csv",
        index=False
    )

    print(f"Saved {len(df)} IOC pulses")

else:

    print("Error:")
    print(response.text)