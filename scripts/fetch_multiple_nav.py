import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}
for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
       response = requests.get(url)
       response.raise_for_status()

       json_data = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


    response = requests.get(url)
    json_data = response.json()

    nav_df = pd.DataFrame(json_data["data"])

    filename = f"data/raw/{scheme_name}.csv"
    nav_df.to_csv(filename, index=False)
    print(f"{scheme_name} downloaded successfully.")

print("\nAll 5 schemes downloaded successfully!")