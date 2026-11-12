# India Foreign Trade Analytics
## Data Sources, Preparation and Analytical Methodology

**Project:** Indian Export Competitiveness & Market Analysis  
**Analysis period:** FY 2021–22 to FY 2025–26  
**Dataset:** India's commodity-wise merchandise exports  
**Technology used:** Python, Pandas  
**Documentation status:** Core data preparation and EDA methodology documented

---

## 1. Data Source

The project uses government trade statistics published through the Government of India's Export Import Data Bank (EIDB), accessible through the Department of Commerce's trade statistics portal.

The analysis uses the commodity-wise export data available through the EIDB portal, with annual export values organized by HS commodity code.

- 2021–22
- 2022–23
- 2023–24
- 2024–25
- 2025–26

The dataset contains export values for 98 HS commodity groups for each financial year.

**Measurement unit:** USD million.

The analysis focuses on merchandise exports and does not include services exports.

## 2. Data Collection and Organization

Commodity-wise export spreadsheets were downloaded for each financial year and organized into a common project structure.

The original spreadsheets were retained separately from the processed dataset to preserve the source data and support verification.

The project follows this directory structure:

```text
India_Foreign_Trade_Analytics/
│
├── DATA/
│   ├── Raw_Data/
│   │   ├── 2021-2022.xlsx
│   │   ├── 2022-2023.xlsx
│   │   ├── 2023-2024.xlsx
│   │   ├── 2024-2025.xlsx
│   │   └── 2025-2026.xlsx
│   │
│   └── Processed_Data/
│       └── india_foreign_trade_master.csv
│
├── Python/
│   ├── 02_validate_dataset.py
│   ├── 03_investigate_growth.py
│   └── 04_exploratory_data_analysis.py
│
└── Reports/
    ├── EDA_Findings.md
    └── Methodology.md
```

The five annual datasets were consolidated into one master dataset to enable consistent year-on-year and commodity-level comparisons.

## 3. Dataset Structure

The processed master dataset contains 490 observations, representing 98 commodity groups across five financial years.

It contains six columns:

| Column | Description |
|---|---|
| `financial_year` | Financial year of the export data |
| `hs_code` | Two-digit Harmonized System commodity code |
| `commodity` | Commodity group description |
| `export_value_usd_mn` | Export value in USD million |
| `share_pct` | Commodity's percentage share of total exports in that year |
| `growth_pct` | Commodity-level export growth percentage |

HS codes are stored as strings to preserve their two-digit format, including leading zeros.

## 4. Data Cleaning and Transformation

The following preparation steps were performed:

1. Imported the annual commodity-wise Excel spreadsheets using Python and Pandas.
2. Standardized the relevant columns across the annual datasets.
3. Retained HS codes as strings to preserve their original format.
4. Combined the five annual datasets into a single master dataset.
5. Checked and corrected an identified inconsistency in the 2023–24 raw spreadsheet values.
6. Calculated commodity export shares and growth percentages.
7. Exported the processed dataset to CSV format for subsequent analysis.

### 4.1 Correction of 2023–24 values

During data verification, the 2023–24 commodity-wise Excel values were found to be doubled relative to the verified annual export total.

The affected commodity values were divided by two during processing.

After correction, the 2023–24 annual export total was USD 437,072.04 million, consistent with the verified official annual total.

The correction was applied to the commodity values rather than changing individual commodity records selectively.

The original raw spreadsheet was retained for reference.

## 5. Dataset Validation

A separate Python validation script was used to assess the structural and numerical consistency of the processed master dataset.

The following checks were performed:

- **Dataset dimensions:** Confirmed 490 observations and six columns.
- **Missing values:** Checked for null or missing values across all columns.
- **Duplicate records:** Checked for duplicate combinations of HS code and financial year.
- **Annual commodity coverage:** Confirmed exactly 98 commodity groups for each financial year.
- **Export share reconciliation:** Verified that commodity shares summed to approximately 100% for each year.
- **Data type consistency:** Ensured HS codes retained their two-digit string format.

All the above validation checks passed.

## 6. Analytical Methodology

The exploratory analysis uses commodity-level and annual export values to examine changes in India's merchandise export composition.

### 6.1 Annual Export Value

Annual merchandise exports are calculated by summing the export values of all 98 commodity groups for each financial year.

\[
Total\ Exports_t = \sum_{i=1}^{98} Export\ Value_{i,t}
\]

Where:

- \(i\) represents a commodity group.
- \(t\) represents a financial year.

### 6.2 Year-on-Year (YoY) Growth

Annual export growth measures the percentage change in total exports compared with the previous financial year.

\[
YoY\ Growth_t =
\frac{Total\ Exports_t - Total\ Exports_{t-1}}
{Total\ Exports_{t-1}} \times 100
\]

The 2021–22 growth rate uses the verified 2020–21 merchandise export total of USD 291,808.48 million as its baseline.

### 6.3 Commodity Export Share

Export share measures the contribution of an individual commodity group to total merchandise exports in a given year.

\[
Share_{i,t} =
\frac{Export\ Value_{i,t}}
{Total\ Exports_t} \times 100
\]

The resulting `share_pct` values are expressed as percentages, not decimal fractions.

### 6.4 Commodity-Level Growth

Commodity-level growth measures the percentage change in the export value of an individual commodity group between consecutive financial years.

\[
Growth_{i,t} =
\frac{Export\ Value_{i,t} - Export\ Value_{i,t-1}}
{Export\ Value_{i,t-1}} \times 100
\]

### 6.5 Compound Annual Growth Rate (CAGR)

CAGR measures the compounded annual rate of change in export value over the five-year observation period.

\[
CAGR =
\left[
\left(\frac{V_{final}}{V_{initial}}\right)^{1/n}
-1
\right]\times 100
\]

Where:

- \(V_{initial}\) is the export value in 2021–22.
- \(V_{final}\) is the export value in 2025–26.
- \(n=4\) annual intervals.

CAGR is interpreted only for commodity groups with positive initial and final export values. It represents the compounded rate of change in nominal export value over four annual intervals.

### 6.6 Absolute Export Change

Absolute export change measures the difference between the final-year and initial-year export values.

\[
Absolute\ Change =
V_{2025-26} - V_{2021-22}
\]

The result is expressed in USD million and helps identify commodity groups with the largest increases or decreases in export value.

### 6.7 Concentration Ratio (CR5 and CR10)

Concentration ratios measure the combined export share of the largest commodity groups.

- **CR5:** Combined export share of the five largest commodity groups.
- **CR10:** Combined export share of the ten largest commodity groups.

The largest commodity groups are identified separately for each financial year.

\[
CR_k = \sum_{i=1}^{k} Share_{i,t}
\]

Where \(k\) represents either 5 or 10.

### 6.8 Herfindahl-Hirschman Index (HHI)

HHI measures the concentration of exports across the 98 commodity groups.

It is calculated as the sum of the squared commodity export shares.

\[
HHI_t = \sum_{i=1}^{98} (Share_{i,t})^2
\]

Export shares are expressed in percentage units when calculating the index.

A higher HHI indicates greater concentration, while a lower HHI indicates a more evenly distributed export composition.

The index is used here as a measure of commodity-level export concentration, not as a direct application of competition-policy thresholds.

### 6.9 Effective Number of Commodity Groups

The effective number of commodity groups translates the HHI into an equivalent number of equally sized groups.

\[
Effective\ Groups = \frac{10,000}{HHI}
\]

This is an equivalent measure of distribution, not the actual number of commodity groups in the dataset.

### 6.10 Commodity-Level HHI Decomposition

To identify which commodity groups contributed to changes in overall export concentration, the change in each commodity's squared share was calculated between two financial years.

\[
Contribution_i = Share_{i,t_2}^{2} - Share_{i,t_1}^{2}
\]

The individual commodity contributions are summed to obtain the aggregate HHI change:

\[
\Delta HHI = \sum_{i=1}^{98} Contribution_i
\]

Each contribution is expressed in HHI points because export shares are measured in percentage units.

This decomposition identifies the mathematical contribution of each commodity group to changes in concentration. It does not independently establish the economic reasons behind those changes.

## 7. Tools and Technologies

| Tool | Application |
|---|---|
| Python | Data preparation, validation and analysis |
| Pandas | Data manipulation and aggregation |
| Excel | Source data inspection and verification |
| PowerShell | Project execution and file management |
| Visual Studio Code | Python development and documentation |
| Git and GitHub | Version control and project management |

SQL-based analysis and Power BI dashboard development are planned subsequent stages of the project.

## 8. Methodological Limitations

The analysis has the following limitations:

1. It covers merchandise exports and excludes services exports.
2. Export values are expressed in nominal USD and are not adjusted for inflation or price changes.
3. Export value growth does not necessarily represent growth in physical export volume.
4. The analysis is conducted across 98 HS commodity groups and does not capture diversification within individual groups.
5. Commodity-level concentration does not measure destination-market or firm-level concentration.
6. Export growth and changes in market share do not independently establish international competitiveness.
7. The analysis identifies statistical patterns but does not establish their economic causes without additional supporting research.
8. HS 99 (Miscellaneous Goods) shows an unusually large decline between 2023–24 and 2024–25. Its underlying economic, classification or reporting explanation remains under investigation.

## 9. Further Methodological Work

The following activities are planned for subsequent project stages:

- Investigate selected commodity-level anomalies using official government sources.
- Conduct additional research into classification and reporting changes where relevant.
- Develop SQL queries for analytical validation and aggregation.
- Build an interactive Power BI dashboard.
- Integrate the analytical findings into a final research report.

---

**Document status:** Core data preparation, validation and EDA methodology documented. Supplementary research and subsequent analytical stages remain in progress.