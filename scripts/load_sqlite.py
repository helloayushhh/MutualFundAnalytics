import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

datasets = {
    "fact_nav": "data/processed/02_nav_history_cleaned.csv",
    "fact_transactions": "data/processed/08_investor_transactions_cleaned.csv",
    "fact_performance": "data/processed/07_scheme_performance_cleaned.csv",
    "fact_aum": "data/raw/03_aum_by_fund_house.csv",
    "dim_fund": "data/raw/01_fund_master.csv"
}
for table_name, file_path in datasets.items():
    df = pd.read_csv(file_path)
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )
    row_count = pd.read_sql(
        f"SELECT COUNT(*) AS total_rows FROM {table_name}",
        engine
    )
    print(f"\n{table_name} loaded successfully!")
    print(row_count)

nav_df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
nav_df["date"] = pd.to_datetime(nav_df["date"])

dates = pd.DataFrame({
    "full_date": nav_df["date"].sort_values().unique()
})
dates["date_id"] = range(1, len(dates) + 1)
dates["day"] = dates["full_date"].dt.day
dates["month"] = dates["full_date"].dt.month
dates["month_name"] = dates["full_date"].dt.month_name()
dates["quarter"] = dates["full_date"].dt.quarter
dates["year"] = dates["full_date"].dt.year
dates["weekday"] = dates["full_date"].dt.day_name()

dates = dates[
    [
        "date_id",
        "full_date",
        "day",
        "month",
        "month_name",
        "quarter",
        "year",
        "weekday"
    ]
]
dates.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)
print("\ndim_date loaded successfully!")
print(
    pd.read_sql(
        "SELECT COUNT(*) AS total_rows FROM dim_date",
        engine
    )
)
print("\nAll datasets loaded into SQLite successfully!")