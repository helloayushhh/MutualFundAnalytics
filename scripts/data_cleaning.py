import pandas as pd

nav_df = pd.read_csv("data/raw/02_nav_history.csv")
transactions_df = pd.read_csv("data/raw/08_investor_transactions.csv")
performance_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 60)
print("NAV HISTORY")
print("=" * 60)

print(nav_df.info())

print("\nMissing Values:")
print(nav_df.isnull().sum())

print("\nDuplicate Rows:")
print(nav_df.duplicated().sum())

print("\n")

print("=" * 60)
print("INVESTOR TRANSACTIONS")
print("=" * 60)

print(transactions_df.info())

print("\nMissing Values:")
print(transactions_df.isnull().sum())

print("\nDuplicate Rows:")
print(transactions_df.duplicated().sum())

print("\n")

print("=" * 60)
print("SCHEME PERFORMANCE")
print("=" * 60)

print(performance_df.info())

print("\nMissing Values:")
print(performance_df.isnull().sum())

print("\nDuplicate Rows:")
print(performance_df.duplicated().sum())

nav_df["date"] = pd.to_datetime(nav_df["date"])

print("\nDate datatype after conversion:")
print(nav_df["date"].dtype)

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)
nav_df = nav_df.drop_duplicates()
invalid_nav = nav_df[nav_df["nav"] <= 0]

print("\nInvalid NAV values:")
print(len(invalid_nav))

nav_df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)
print("\nCleaned NAV dataset saved successfully.")

# Convert transaction_date to datetime
transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"]
)
print("\nTransaction Date datatype:")
print(transactions_df["transaction_date"].dtype)

print("\nTransaction Types:")
print(transactions_df["transaction_type"].unique())
transactions_df["transaction_type"] = (
    transactions_df["transaction_type"]
    .str.strip()
    .str.title()
)

invalid_amount = transactions_df[
    transactions_df["amount_inr"] <= 0
]
print("\nInvalid Amount Records:")
print(len(invalid_amount))

print("\nKYC Status:")
print(transactions_df["kyc_status"].unique())

transactions_df = transactions_df.drop_duplicates()
transactions_df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)
print("\nCleaned investor_transactions dataset saved successfully.")

numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]
performance_df[numeric_columns] = performance_df[numeric_columns].apply(
    pd.to_numeric,
    errors="coerce"
)
print("\nMissing values after numeric conversion:")
print(performance_df[numeric_columns].isnull().sum())

invalid_expense = performance_df[
    (performance_df["expense_ratio_pct"] < 0.1) |
    (performance_df["expense_ratio_pct"] > 2.5)
]
print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))
performance_df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)
print("\nCleaned scheme_performance dataset saved successfully.")