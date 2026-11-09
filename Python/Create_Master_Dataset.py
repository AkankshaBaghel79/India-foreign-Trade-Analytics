import pandas as pd

# ============================================================
# PROJECT FILES
# ============================================================

files = {
    "2021-22": ("DATA/Raw_Data/2021-2022.xlsx", "2021 - 2022"),
    "2022-23": ("DATA/Raw_Data/2022-2023.xlsx", "2022 - 2023"),
    "2023-24": ("DATA/Raw_Data/2023-2024.xlsx", "2023 - 2024"),
    "2024-25": ("DATA/Raw_Data/2024-2025.xlsx", "2024 - 2025"),
    "2025-26": ("DATA/Raw_Data/2025-2026.xlsx", "2025 - 2026")
}


# ============================================================
# FUNCTION TO PROCESS EACH YEAR
# ============================================================

def process_file(file_path, financial_year, year_column):

    # Read Excel file
    df = pd.read_excel(
        file_path,
        header=2
    )

    # Remove total row
    commodity_df = df[
        df["HSCode"] != "India's Total Export"
    ].copy()

    # Keep required columns
    clean_df = commodity_df[
        ["HSCode", "Commodity", year_column]
    ].copy()

    # Rename columns
    clean_df.columns = [
        "hs_code",
        "commodity",
        "export_value_usd_mn"
    ]

    # Standardize HS codes
    clean_df["hs_code"] = (
        clean_df["hs_code"]
        .astype(str)
        .str.strip()
        .str.zfill(2)
    )

    # Correct 2023-24 commodity values
    if financial_year == "2023-24":
        clean_df["export_value_usd_mn"] = (
            clean_df["export_value_usd_mn"] / 2
        )

    # Add financial year
    clean_df["financial_year"] = financial_year

    return clean_df


# ============================================================
# PROCESS ALL FIVE PROJECT YEARS
# ============================================================

all_years = []

for financial_year, (file_path, year_column) in files.items():

    yearly_data = process_file(
        file_path,
        financial_year,
        year_column
    )

    all_years.append(yearly_data)


# ============================================================
# CREATE MASTER DATASET
# ============================================================

master_df = pd.concat(
    all_years,
    ignore_index=True
)


# ============================================================
# SORT DATA
# ============================================================

year_order = [
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26"
]

master_df["financial_year"] = pd.Categorical(
    master_df["financial_year"],
    categories=year_order,
    ordered=True
)

master_df["_hs_sort"] = master_df["hs_code"].astype(int)

master_df = (
    master_df
    .sort_values(
        ["_hs_sort", "financial_year"]
    )
    .drop(columns="_hs_sort")
    .reset_index(drop=True)
)


# ============================================================
# VALIDATE MASTER DATASET
# ============================================================

duplicates = master_df.duplicated(
    subset=["financial_year", "hs_code"]
).sum()


# ============================================================
# CALCULATE EXPORT SHARE
# ============================================================

yearly_totals = (
    master_df
    .groupby(
        "financial_year",
        observed=True
    )["export_value_usd_mn"]
    .transform("sum")
)

master_df["share_pct"] = (
    master_df["export_value_usd_mn"]
    / yearly_totals
    * 100
)


# ============================================================
# CALCULATE YEAR-ON-YEAR GROWTH
# ============================================================

# ------------------------------------------------------------
# Get 2020-21 baseline from the 2021-22 source file
# ------------------------------------------------------------

baseline_df = pd.read_excel(
    "DATA/Raw_Data/2021-2022.xlsx",
    header=2
)

# Remove total row
baseline_df = baseline_df[
    baseline_df["HSCode"] != "India's Total Export"
].copy()

# Keep only HS code and 2020-21 exports
baseline_df = baseline_df[
    ["HSCode", "2020 - 2021"]
].copy()

# Rename columns
baseline_df.columns = [
    "hs_code",
    "baseline_2020_21"
]

# Standardize HS codes
baseline_df["hs_code"] = (
    baseline_df["hs_code"]
    .astype(str)
    .str.strip()
    .str.zfill(2)
)

# Create lookup dictionary
baseline_lookup = (
    baseline_df
    .set_index("hs_code")["baseline_2020_21"]
)


# ------------------------------------------------------------
# Previous-year export values
# ------------------------------------------------------------

master_df["previous_year_export"] = (
    master_df
    .groupby(
        "hs_code",
        observed=True
    )["export_value_usd_mn"]
    .shift(1)
)


# ------------------------------------------------------------
# Replace 2021-22 previous-year values with 2020-21 baseline
# ------------------------------------------------------------

first_year_mask = (
    master_df["financial_year"] == "2021-22"
)

master_df.loc[
    first_year_mask,
    "previous_year_export"
] = (
    master_df.loc[
        first_year_mask,
        "hs_code"
    ].map(baseline_lookup)
)


# ------------------------------------------------------------
# Calculate growth
# ------------------------------------------------------------

master_df["growth_pct"] = (
    (
        master_df["export_value_usd_mn"]
        / master_df["previous_year_export"]
    ) - 1
) * 100


# Remove temporary column
master_df = master_df.drop(
    columns="previous_year_export"
)


# ============================================================
# FINAL COLUMN ORDER
# ============================================================

master_df = master_df[
    [
        "financial_year",
        "hs_code",
        "commodity",
        "export_value_usd_mn",
        "share_pct",
        "growth_pct"
    ]
]

# ============================================================
# SAVE PROCESSED DATASET
# ============================================================

output_path = "DATA/Processed_Data/india_foreign_trade_master.csv"

master_df.to_csv(
    output_path,
    index=False
)

print("\nProcessed dataset saved successfully:")
print(output_path)