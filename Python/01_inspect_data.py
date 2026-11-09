import pandas as pd

file_path = r"DATA\Raw_Data\2023-2024.xlsx"

df = pd.read_excel(file_path, header=2)

# Separate the total row
total_row = df[df["HSCode"] == "India's Total Export"].copy()

# Keep only commodity rows
commodity_df = df[df["HSCode"] != "India's Total Export"].copy()

# Keep only the columns we need
clean_df = commodity_df[[
    "HSCode",
    "Commodity",
    "2023 - 2024"
]].copy()

# Rename columns
clean_df.columns = [
    "hs_code",
    "commodity",
    "export_value_usd_mn"
]

# IMPORTANT:
# The 2023-24 commodity values in this EIDB file are doubled.
# Correct the commodity values by dividing by 2.
clean_df["export_value_usd_mn"] = (
    clean_df["export_value_usd_mn"] / 2
)

# Add financial year
clean_df["financial_year"] = "2023-24"

print(clean_df.head())

print("\nColumns:")
print(clean_df.columns.tolist())

print("\nShape:")
print(clean_df.shape)

print("\nTotal export from EIDB:")
print(total_row[["HSCode", "2023 - 2024"]])

print("\nSum of corrected commodity exports:")
print(clean_df["export_value_usd_mn"].sum())