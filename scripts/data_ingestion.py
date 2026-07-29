import pandas as pd
import os

folder_path = "data/raw"
csv_files = [
    file
    for file in os.listdir(folder_path)
    if file.endswith(".csv")
]

for file in csv_files:
    print("=" * 70)
    print(f"Reading: {file}")
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")