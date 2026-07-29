import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("UNIQUE FUND HOUSES")
print("=" * 60)
print(df["fund_house"].unique())

print("\n")

print("=" * 60)
print("UNIQUE CATEGORIES")
print("=" * 60)
print(df["category"].unique())

print("\n")

print("=" * 60)
print("UNIQUE SUB-CATEGORIES")
print("=" * 60)
print(df["sub_category"].unique())

print("\n")

print("=" * 60)
print("UNIQUE RISK CATEGORIES")
print("=" * 60)
print(df["risk_category"].unique())