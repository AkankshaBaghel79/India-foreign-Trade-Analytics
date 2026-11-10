
import pandas as pd

# Load processed master dataset
file_path = "DATA/Processed_Data/india_foreign_trade_master.csv"
df = pd.read_csv(file_path)

print("\n========== DATASET OVERVIEW ==========")
print("Dataset shape:", df.shape)
print("\nData types:")
print(df.dtypes)

# 1. Annual export totals
print("\n========== ANNUAL EXPORT TOTALS ==========")

annual_summary = df.groupby("financial_year").agg(
    total_exports_usd_mn=("export_value_usd_mn", "sum"),
    total_commodities=("hs_code", "nunique"),
    total_share_pct=("share_pct", "sum")
).round(2)

print(annual_summary)

# 2. Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 3. Duplicate records
print("\n========== DUPLICATE CHECK ==========")
print("Duplicate HS code/year records:",
      df.duplicated(subset=["financial_year", "hs_code"]).sum())

# 4. Commodity count
print("\n========== COMMODITY COUNT ==========")
print(df.groupby("financial_year")["hs_code"].nunique())

# 5. Growth data check
print("\n========== GROWTH DATA ==========")
print(df["growth_pct"].describe().round(2))

print("\nDataset validation completed.")
