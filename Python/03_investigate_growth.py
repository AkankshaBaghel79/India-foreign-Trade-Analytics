
import pandas as pd

# Load the processed master dataset
file_path = r"DATA\Processed_Data\india_foreign_trade_master.csv"

df = pd.read_csv(file_path, dtype={"hs_code": str})

# -----------------------------------------
# 1. IDENTIFY THE 10 LOWEST GROWTH COMMODITIES
# -----------------------------------------

print("\n========== 10 LOWEST GROWTH COMMODITIES ==========")

lowest_growth = df.sort_values("growth_pct").head(10)

print(
    lowest_growth[
        ["financial_year", "hs_code", "commodity",
         "export_value_usd_mn", "growth_pct"]
    ].to_string(index=False)
)

# -----------------------------------------
# 2. IDENTIFY THE COMMODITY WITH MINIMUM GROWTH
# -----------------------------------------

worst = df.loc[df["growth_pct"].idxmin()]

print("\n========== WORST PERFORMING COMMODITY ==========")

print("Financial Year:", worst["financial_year"])
print("HS Code:", worst["hs_code"])
print("Commodity:", worst["commodity"])
print("Current Export Value (USD million):", worst["export_value_usd_mn"])
print("Growth Rate:", worst["growth_pct"], "%")

# -----------------------------------------
# 3. CALCULATE IMPLIED PREVIOUS-YEAR EXPORT VALUE
# -----------------------------------------

growth_factor = 1 + (worst["growth_pct"] / 100)

if growth_factor > 0:
    previous_export = worst["export_value_usd_mn"] / growth_factor

    print("\n========== PREVIOUS YEAR COMPARISON ==========")
    print("Implied Previous Year Export Value (USD million):",
          round(previous_export, 2))
    print("Current Year Export Value (USD million):",
          round(worst["export_value_usd_mn"], 2))
else:
    print("Previous-year value cannot be calculated.")

# -----------------------------------------
# 4. CHECK THE COMMODITY'S FIVE-YEAR HISTORY
# -----------------------------------------

print("\n========== COMMODITY EXPORT HISTORY ==========")

commodity_history = df[df["hs_code"] == worst["hs_code"]].sort_values(
    "financial_year"
)

print(
    commodity_history[
        ["financial_year", "hs_code", "commodity",
         "export_value_usd_mn", "share_pct", "growth_pct"]
    ].to_string(index=False)
)

print("\nGrowth investigation completed.")
