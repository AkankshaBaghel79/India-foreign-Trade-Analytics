
import pandas as pd

# ==========================================
# INDIA FOREIGN TRADE ANALYTICS
# EXPLORATORY DATA ANALYSIS
# ==========================================

# Load cleaned master dataset
file_path = r"DATA\Processed_Data\india_foreign_trade_master.csv"

df = pd.read_csv(file_path, dtype={"hs_code": str})

# ==========================================
# 1. ANNUAL EXPORT PERFORMANCE
# ==========================================

annual_exports = (
    df.groupby("financial_year")
    .agg(
        total_exports_usd_mn=("export_value_usd_mn", "sum"),
        total_commodities=("hs_code", "count")
    )
    .reset_index()
)


# ==========================================
# CALCULATE ANNUAL YOY GROWTH
# ==========================================

# Verified 2020-21 total exports (USD million)
baseline_2020_21 = 291808.48

# Calculate year-on-year growth
annual_exports["yoy_growth_pct"] = (
    annual_exports["total_exports_usd_mn"].pct_change() * 100
)

# Calculate 2021-22 growth using 2020-21 baseline
annual_exports.loc[
    annual_exports["financial_year"] == "2021-22",
    "yoy_growth_pct"
] = (
    (annual_exports.loc[
        annual_exports["financial_year"] == "2021-22",
        "total_exports_usd_mn"
    ] / baseline_2020_21) - 1
) * 100


# Format numerical values
annual_exports["total_exports_usd_mn"] = (
    annual_exports["total_exports_usd_mn"].round(2)
)

annual_exports["yoy_growth_pct"] = (
    annual_exports["yoy_growth_pct"].round(2)
)

# Display results
# print("\n========== ANNUAL EXPORT PERFORMANCE ==========")

# print(annual_exports.to_string(index=False))

# ==========================================
# 2. HIGHEST AND LOWEST EXPORT YEARS
# ==========================================

highest_year = annual_exports.loc[
    annual_exports["total_exports_usd_mn"].idxmax()
]

lowest_year = annual_exports.loc[
    annual_exports["total_exports_usd_mn"].idxmin()
]

# print("\n========== EXPORT PERFORMANCE HIGHLIGHTS ==========")

# print(
#     f"Highest exports: {highest_year['financial_year']} "
#     f"(USD {highest_year['total_exports_usd_mn']} million)"
# )

# print(
#     f"Lowest exports: {lowest_year['financial_year']} "
#     f"(USD {lowest_year['total_exports_usd_mn']} million)"
# )

# print("\nAnnual export analysis completed.")

# ==========================================
# 3. TOP 10 EXPORT COMMODITIES - 2025-26
# ==========================================

latest_year = "2025-26"

latest_data = df[
    df["financial_year"] == latest_year
].copy()

# Sort commodities by export value
top_10 = latest_data.sort_values(
    by="export_value_usd_mn",
    ascending=False
).head(10).copy()

# Calculate combined contribution of top 10
top_10_share = top_10["share_pct"].sum()

# print("\n========== TOP 10 EXPORT COMMODITIES - 2025-26 ==========")

# print(
#     top_10[
#         ["hs_code", "commodity", "export_value_usd_mn", "share_pct"]
#     ].to_string(index=False)
# )

# print("\n========== TOP 10 EXPORT CONCENTRATION ==========")

# print(
#     f"Combined export value: USD "
#     f"{top_10['export_value_usd_mn'].sum():,.2f} million"
# )

# print(f"Combined share of total exports: {top_10_share:.2f}%")

# print(
#     f"Remaining commodities' share: "
#     f"{100 - top_10_share:.2f}%"
# )

# print("\nTop 10 commodity analysis completed.")

# ==========================================
# 4. FIVE-YEAR EXPORT TRENDS OF TOP 10
# ==========================================

# Get HS codes of the top 10 commodities in 2025-26
top_10_codes = top_10["hs_code"].tolist()

# Filter these commodities across all five years
top_10_trends = df[
    df["hs_code"].isin(top_10_codes)
].copy()

# Create a year-wise export value comparison
export_trend = top_10_trends.pivot(
    index=["hs_code", "commodity"],
    columns="financial_year",
    values="export_value_usd_mn"
).reset_index()

# Round export values
year_columns = [
    "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"
]

export_trend[year_columns] = export_trend[year_columns].round(2)

# print("\n========== FIVE-YEAR EXPORT TRENDS: TOP 10 COMMODITIES ==========")
# print(export_trend.to_string(index=False))

# print("\nFive-year export trend analysis completed.")

# ==========================================
# 5. TOP 10 COMMODITY GROWTH ANALYSIS
# ==========================================

export_trend["total_growth_pct"] = (
    (
        export_trend["2025-26"] /
        export_trend["2021-22"]
    ) - 1
) * 100

export_trend["cagr_pct"] = (
    (
        export_trend["2025-26"] /
        export_trend["2021-22"]
    ) ** (1 / 4) - 1
) * 100

# Round calculated percentages
export_trend["total_growth_pct"] = (
    export_trend["total_growth_pct"].round(2)
)

export_trend["cagr_pct"] = (
    export_trend["cagr_pct"].round(2)
)

# Sort by CAGR
growth_analysis = export_trend.sort_values(
    by="cagr_pct",
    ascending=False
)

# print("\n========== TOP 10 COMMODITY GROWTH ANALYSIS ==========")

# print(
#     growth_analysis[
#         ["hs_code", "commodity", "total_growth_pct", "cagr_pct"]
#     ].to_string(index=False)
# )

# print("\nCommodity growth analysis completed.")

# ==========================================
# 6. CHANGE IN EXPORT SHARE - TOP 10
# ==========================================

# Create a year-wise pivot of export shares
share_trend = top_10_trends.pivot(
    index=["hs_code", "commodity"],
    columns="financial_year",
    values="share_pct"
).reset_index()

# Calculate change in export share (percentage points)
share_trend["share_change_pp"] = (
    share_trend["2025-26"] - share_trend["2021-22"]
).round(2)

# Round annual shares
share_trend[year_columns] = (
    share_trend[year_columns].round(2)
)

# Sort by change in export share
share_analysis = share_trend.sort_values(
    by="share_change_pp",
    ascending=False
)

# print("\n========== CHANGE IN EXPORT SHARE: TOP 10 ==========")

# print(
#     share_analysis[
#         [
#             "hs_code",
#             "commodity",
#             "2021-22",
#             "2025-26",
#             "share_change_pp"
#         ]
#     ].to_string(index=False)
# )

# print("\nExport share analysis completed.")

# ==========================================
# 7. EXPORT SHARE CHANGES - ALL COMMODITIES
# ==========================================

all_share_trends = df.pivot(
    index=["hs_code", "commodity"],
    columns="financial_year",
    values="share_pct"
).reset_index()

# Calculate change in export share
all_share_trends["share_change_pp"] = (
    all_share_trends["2025-26"] -
    all_share_trends["2021-22"]
).round(2)

# Identify top 10 gainers
top_gainers = all_share_trends.sort_values(
    by="share_change_pp",
    ascending=False
).head(10)

# Identify top 10 decliners
top_decliners = all_share_trends.sort_values(
    by="share_change_pp",
    ascending=True
).head(10)

# print("\n========== TOP 10 COMMODITY SHARE GAINERS ==========")

# print(
#     top_gainers[
#         ["hs_code", "commodity", "2021-22", "2025-26", "share_change_pp"]
#     ].to_string(index=False)
# )

# print("\n========== TOP 10 COMMODITY SHARE DECLINERS ==========")

# print(
#     top_decliners[
#         ["hs_code", "commodity", "2021-22", "2025-26", "share_change_pp"]
#     ].to_string(index=False)
# )

# print("\nAll-commodity export share analysis completed.")

# ==========================================
# 8. CAGR ANALYSIS - ALL 98 COMMODITIES
# ==========================================

# Create a year-wise export value table
all_export_trends = df.pivot(
    index=["hs_code", "commodity"],
    columns="financial_year",
    values="export_value_usd_mn"
).reset_index()

# Calculate total export value growth
all_export_trends["total_growth_pct"] = (
    (
        all_export_trends["2025-26"] /
        all_export_trends["2021-22"]
    ) - 1
) * 100

# Calculate four-year CAGR
all_export_trends["cagr_pct"] = (
    (
        all_export_trends["2025-26"] /
        all_export_trends["2021-22"]
    ) ** (1 / 4) - 1
) * 100

# Round calculated percentages
all_export_trends["total_growth_pct"] = (
    all_export_trends["total_growth_pct"].round(2)
)

all_export_trends["cagr_pct"] = (
    all_export_trends["cagr_pct"].round(2)
)

# Identify fastest-growing commodities
top_10_cagr = all_export_trends.sort_values(
    by="cagr_pct",
    ascending=False
).head(10)

# Identify commodities with the lowest CAGR
bottom_10_cagr = all_export_trends.sort_values(
    by="cagr_pct",
    ascending=True
).head(10)

# print("\n========== TOP 10 FASTEST-GROWING COMMODITIES ==========")

# print(
#     top_10_cagr[
#         ["hs_code", "commodity", "total_growth_pct", "cagr_pct"]
#     ].to_string(index=False)
# )

# print("\n========== TOP 10 SLOWEST-GROWING COMMODITIES ==========")

# print(
#     bottom_10_cagr[
#         ["hs_code", "commodity", "total_growth_pct", "cagr_pct"]
#     ].to_string(index=False)
# )

# print("\nAll-commodity CAGR analysis completed.")

# ==========================================
# 9. EXPORT VALUE COMPARISON - FASTEST AND SLOWEST
# ==========================================

# Calculate absolute change in export value
all_export_trends["export_change_usd_mn"] = (
    all_export_trends["2025-26"] -
    all_export_trends["2021-22"]
).round(2)

# Get latest export share
latest_shares = df[
    df["financial_year"] == "2025-26"
][["hs_code", "share_pct"]]

all_export_trends = all_export_trends.merge(
    latest_shares,
    on="hs_code",
    how="left"
)

# Refresh rankings
top_10_cagr = all_export_trends.sort_values(
    by="cagr_pct",
    ascending=False
).head(10)

bottom_10_cagr = all_export_trends.sort_values(
    by="cagr_pct",
    ascending=True
).head(10)

columns_to_display = [
    "hs_code",
    "commodity",
    "2021-22",
    "2025-26",
    "export_change_usd_mn",
    "cagr_pct",
    "share_pct"
]

# print("\n========== EXPORT VALUE: FASTEST-GROWING COMMODITIES ==========")

# print(
#     top_10_cagr[columns_to_display].to_string(index=False)
# )

# print("\n========== EXPORT VALUE: SLOWEST-GROWING COMMODITIES ==========")

# print(
#     bottom_10_cagr[columns_to_display].to_string(index=False)
# )

# print("\nExport value comparison completed.")

# ==========================================
# 10. LARGEST ABSOLUTE EXPORT CHANGES
# ==========================================

# Top 10 commodities with the largest export increases
top_absolute_gainers = all_export_trends.sort_values(
    by="export_change_usd_mn",
    ascending=False
).head(10)

# Top 10 commodities with the largest export decreases
top_absolute_decliners = all_export_trends.sort_values(
    by="export_change_usd_mn",
    ascending=True
).head(10)

columns_to_display = [
    "hs_code",
    "commodity",
    "2021-22",
    "2025-26",
    "export_change_usd_mn",
    "cagr_pct",
    "share_pct"
]

# print("\n========== TOP 10 COMMODITIES BY EXPORT INCREASE ==========")

# print(
#     top_absolute_gainers[columns_to_display].to_string(index=False)
# )

# print("\n========== TOP 10 COMMODITIES BY EXPORT DECREASE ==========")

# print(
#     top_absolute_decliners[columns_to_display].to_string(index=False)
# )

# print("\nAbsolute export change analysis completed.")


# ==========================================
# 11. EXPORT CONCENTRATION ANALYSIS
# ==========================================

concentration_results = []

for year in sorted(df["financial_year"].unique()):

    year_data = df[
        df["financial_year"] == year
    ].sort_values(
        by="share_pct",
        ascending=False
    )

    # Concentration ratios
    cr5 = year_data.head(5)["share_pct"].sum()
    cr10 = year_data.head(10)["share_pct"].sum()

    # Herfindahl-Hirschman Index
    hhi = (year_data["share_pct"] ** 2).sum()

    concentration_results.append({
        "financial_year": year,
        "cr5_pct": cr5,
        "cr10_pct": cr10,
        "hhi": hhi
    })

concentration_df = pd.DataFrame(concentration_results)

# print("\n========== EXPORT CONCENTRATION ANALYSIS ==========")

# print(
#     concentration_df.round(2).to_string(index=False)
# )

# print("\nExport concentration analysis completed.")


# ==========================================
# 12. EFFECTIVE NUMBER OF COMMODITY GROUPS
# ==========================================

concentration_df["effective_groups"] = (
    10000 / concentration_df["hhi"]
)

# print("\n========== EXPORT DIVERSIFICATION ANALYSIS ==========")

# print(
#     concentration_df[
#         ["financial_year", "hhi", "effective_groups"]
#     ].round(2).to_string(index=False)
# )

# print("\nEffective commodity group analysis completed.")


# ==========================================
# 13. COMMODITY CONTRIBUTION TO HHI
# ==========================================

# Compare HHI contributions across years
hhi_contributions = df[
    df["financial_year"].isin(["2021-22", "2022-23", "2025-26"])
].copy()

hhi_contributions["hhi_contribution"] = (
    hhi_contributions["share_pct"] ** 2
)

hhi_pivot = hhi_contributions.pivot(
    index=["hs_code", "commodity"],
    columns="financial_year",
    values="hhi_contribution"
).reset_index()

# Change in HHI contribution
hhi_pivot["change_2021_22_to_2022_23"] = (
    hhi_pivot["2022-23"] - hhi_pivot["2021-22"]
)

hhi_pivot["change_2022_23_to_2025_26"] = (
    hhi_pivot["2025-26"] - hhi_pivot["2022-23"]
)

# Largest contributors to concentration increase
top_hhi_increases = hhi_pivot.sort_values(
    by="change_2021_22_to_2022_23",
    ascending=False
).head(10)

# print("\n========== COMMODITIES DRIVING CONCENTRATION INCREASE ==========")

# print(
#     top_hhi_increases[
#         ["hs_code", "commodity", "change_2021_22_to_2022_23"]
#     ].round(2).to_string(index=False)
# )

# Largest contributors to concentration reduction
top_hhi_reductions = hhi_pivot.sort_values(
    by="change_2022_23_to_2025_26",
    ascending=True
).head(10)

# print("\n========== COMMODITIES DRIVING CONCENTRATION REDUCTION ==========")

# print(
#     top_hhi_reductions[
#         ["hs_code", "commodity", "change_2022_23_to_2025_26"]
#     ].round(2).to_string(index=False)
# )

# print("\nHHI contribution analysis completed.")


# ==========================================
# 14. HHI RECONCILIATION CHECK
# ==========================================

# Sum contribution changes across all 98 commodities
change_1 = hhi_pivot[
    "change_2021_22_to_2022_23"
].sum()

change_2 = hhi_pivot[
    "change_2022_23_to_2025_26"
].sum()

# Compare with aggregate HHI changes
aggregate_change_1 = (
    concentration_df.loc[1, "hhi"]
    - concentration_df.loc[0, "hhi"]
)

aggregate_change_2 = (
    concentration_df.loc[4, "hhi"]
    - concentration_df.loc[1, "hhi"]
)

print("\n========== HHI RECONCILIATION CHECK ==========")

print(f"2021-22 to 2022-23:")
print(f"Sum of commodity contributions: {change_1:.2f}")
print(f"Aggregate HHI change:           {aggregate_change_1:.2f}")

print(f"\n2022-23 to 2025-26:")
print(f"Sum of commodity contributions: {change_2:.2f}")
print(f"Aggregate HHI change:           {aggregate_change_2:.2f}")

print("\nHHI reconciliation completed.")
