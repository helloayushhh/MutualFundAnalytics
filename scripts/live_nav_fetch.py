import requests
import pandas as pd
url = "https://api.mfapi.in/mf/125497"

try:
    response = requests.get(url)
    response.raise_for_status()

    json_data = response.json()
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

nav_df = pd.DataFrame(json_data["data"])
print(nav_df.head())

nav_df.to_csv(
    "data/raw/live_nav_125497.csv",
    index=False
)
print("csv saved successfully!")