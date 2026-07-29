import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

if len(missing_codes) == 0:
    print("All AMFI codes are present in nav_history.csv")
else:
    print("Missing AMFI Codes:")
    print(missing_codes)