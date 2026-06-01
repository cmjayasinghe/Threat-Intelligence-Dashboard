import requests
import pandas as pd

print("Fetching ransomware victims...")

url = "https://api.ransomware.live/recentvictims"

response = requests.get(
    url,
    timeout=30
)

print("Status Code:", response.status_code)

if response.status_code == 200:

    data = response.json()

    df = pd.DataFrame(data)

    df.to_csv(
        "data/ransomware.csv",
        index=False
    )

    print(f"Saved {len(df)} ransomware records")

else:

    print("Failed to retrieve data")
    print(response.text)