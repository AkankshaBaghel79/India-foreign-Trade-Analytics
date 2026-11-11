# India Foreign Trade Analytics
## Exploratory Data Analysis – Findings Report

**Project:** Indian Export Competitiveness & Market Analysis  
**Analysis period:** FY 2021–22 to FY 2025–26  
**Dataset:** India's commodity-wise merchandise exports  
**Commodity coverage:** 98 HS commodity groups (HS 01–99 as represented in the dataset)  
**Technology:** Python, Pandas

**Document status:** EDA in progress

---

## 1. Project Overview

This analysis examines India's merchandise export performance across 98 commodity groups over five financial years, from 2021–22 to 2025–26.

The objective is to identify major export categories, understand changes in export values and shares, examine commodity-level growth, and assess the concentration and diversification of India's export basket.

The analysis uses government trade data and Python-based data processing and exploratory analysis.

## 2. Dataset Overview and Validation

The processed master dataset contains:

- 490 observations.
- 98 commodity groups per financial year.
- Five financial years.
- Six columns: financial_year, hs_code, commodity, export_value_usd_mn, share_pct and growth_pct.

### Data validation results

- No missing values.
- No duplicate HS-code and financial-year combinations.
- Exactly 98 commodity groups for each financial year.
- Commodity export shares sum to approximately 100% for each year.

### Data cleaning note

The raw 2023–24 commodity-wise Excel values were found to be doubled. These values were divided by two during data cleaning. The corrected annual export total is USD 437,072.04 million and matches the verified official annual total.

This correction is documented as part of the data preparation process.

## 3. Annual Export Performance

| Financial Year | Total Exports (USD million) | Annual Growth |
|---|---:|---:|
| 2021–22 | 422,004.40 | 44.62% |
| 2022–23 | 451,069.97 | 6.89% |
| 2023–24 | 437,072.04 | -3.10% |
| 2024–25 | 437,704.55 | 0.14% |
| 2025–26 | 441,452.19 | 0.86% |

The 2021–22 growth rate is calculated against the verified 2020–21 merchandise export total of USD 291,808.48 million.

**Key observations:**

- Highest annual exports were recorded in 2022–23.
- Exports declined in 2023–24.
- Exports recovered modestly during 2024–25 and 2025–26.
- Overall merchandise exports increased by approximately USD 19.45 billion between 2021–22 and 2025–26.

## 4. Major Export Commodity Groups

The ten largest export commodity groups in 2025–26 accounted for approximately 63.20% of total exports.

Leading categories included:

1. Mineral fuels and oils (HS 27): USD 55.87 billion.
2. Electrical machinery (HS 85): USD 53.98 billion.
3. Machinery and mechanical appliances (HS 84): USD 36.63 billion.
4. Precious stones and jewellery (HS 71): USD 28.34 billion.
5. Vehicles (HS 87): USD 25.97 billion.
6. Pharmaceuticals (HS 30): USD 25.07 billion.

The top two categories, HS 27 and HS 85, together accounted for approximately 24.88% of exports.

## 5. Commodity Growth Analysis

The CAGR analysis compared export values between 2021–22 and 2025–26 using four annual intervals.

### Important growth observations

- Electrical machinery (HS 85) recorded a CAGR of 27.89%.
- Machinery (HS 84) recorded a CAGR of 9.57%.
- Vehicles (HS 87) recorded a CAGR of 7.07%.
- Pharmaceuticals (HS 30) recorded a CAGR of 6.63%.

Electrical machinery was particularly significant because its exports increased by approximately USD 33.80 billion and its export share rose from 4.78% to 12.23%.

### Major declining categories

- Iron and steel (HS 72): CAGR -18.08%.
- Cotton (HS 52): CAGR -13.70%.
- Aluminium (HS 76): CAGR -9.81%.
- Organic chemicals (HS 29): CAGR -1.91%.

These results represent changes in nominal export values, not necessarily changes in physical export volumes or international competitiveness.

## 6. Absolute Export Changes

The largest absolute export increases between 2021–22 and 2025–26 included:

| Commodity | Change (USD million) |
|---|---:|
| Electrical machinery (HS 85) | +33,797.56 |
| Machinery (HS 84) | +11,219.55 |
| Vehicles (HS 87) | +6,210.88 |
| Pharmaceuticals (HS 30) | +5,677.14 |

The largest absolute declines included:

| Commodity | Change (USD million) |
|---|---:|
| Mineral fuels (HS 27) | -13,698.80 |
| Iron and steel (HS 72) | -12,589.64 |
| Precious stones and jewellery (HS 71) | -10,924.78 |
| Cotton (HS 52) | -4,804.02 |

The findings indicate that export growth was uneven across commodity groups, with substantial increases in some categories offset by declines in others.

## 7. Export Concentration and Diversification

Three principal indicators were used:

- CR5: Combined export share of the five largest commodity groups.
- CR10: Combined export share of the ten largest commodity groups.
- HHI: Herfindahl-Hirschman Index, calculated as the sum of squared commodity export shares expressed in percentage units.

### Five-year results

| Financial Year | CR5 (%) | CR10 (%) | HHI | Effective Groups |
|---|---:|---:|---:|---:|
| 2021–22 | 42.46 | 62.13 | 577.19 | 17.33 |
| 2022–23 | 48.07 | 65.39 | 774.00 | 12.92 |
| 2023–24 | 47.37 | 64.30 | 690.38 | 14.48 |
| 2024–25 | 45.49 | 62.61 | 576.74 | 17.34 |
| 2025–26 | 45.48 | 63.20 | 562.23 | 17.79 |

The effective number of commodity groups is calculated as 10,000 divided by HHI. It represents the number of equally sized groups that would produce the observed HHI; it is not the actual number of commodity groups.

### Key findings

1. The HHI increased substantially in 2022–23, from 577.19 to 774.00.
2. The HHI subsequently declined to 562.23 in 2025–26.
3. Over the full five-year period, HHI declined by approximately 2.59%.
4. The effective number of commodity groups increased from 17.33 to 17.79.
5. CR5 and CR10 increased slightly between the first and last years, indicating that the largest categories collectively retained or increased their share of exports.

These indicators provide a mixed picture: overall concentration declined modestly, while the combined share of the largest five and ten categories increased.

### Commodity-level HHI decomposition

The increase in HHI between 2021–22 and 2022–23 was 196.81 points.

Mineral fuels (HS 27) contributed +231.99 points to this increase, making it the dominant contributor. Electrical machinery (HS 85) contributed +17.36 points.

Between 2022–23 and 2025–26, HHI declined by 211.77 points. Mineral fuels contributed -343.59 points to this decline, followed by precious stones and jewellery (HS 71) at -30.17 points.

The sum of individual commodity contribution changes matched the aggregate HHI changes in both periods, validating the decomposition.

## 8. Data Anomalies and Research Questions

### HS 99 – Miscellaneous Goods

HS 99 exports declined from USD 93.925 million in 2023–24 to USD 0.310 million in 2024–25, a decline of approximately 99.67%.

The 2023–24 raw Excel value was 187.85 million and was divided by two during the documented data correction.

The 2024–25 raw value was 0.310 million, matching the processed dataset.

The arithmetic and cleaning correction have been checked. However, the underlying reason for the decline remains unresolved.

**Further investigation required:** Determine whether the change reflects economic developments, classification changes, reporting practices or another factor using official government sources.

HS 99 has been retained in the dataset without adjustment.

## 9. Methodological Limitations

- The analysis covers merchandise exports, not services exports.
- Values are expressed in nominal USD and do not measure physical export volumes.
- The dataset uses 98 HS commodity groups, so it does not capture diversification within individual groups.
- Commodity diversification does not establish destination-market or firm-level diversification.
- Growth in export value or share alone does not establish international competitiveness.
- Economic explanations for major changes require further research and supporting evidence.

## 10. Further Work

The following activities remain planned:

- Investigate major commodity-level movements using official sources.
- Examine HS 99 and other unusual movements.
- Conduct additional analysis of export concentration and diversification where useful.
- Develop SQL-based analytical queries.
- Build an interactive Power BI dashboard.
- Prepare a final research report with conclusions and visualizations.

---

**Report status:** Preliminary analytical findings. This document will be updated as the project progresses.