# Mutual Fund Analytics - Data Dictionary

## Overview

This document describes the datasets used in the Mutual Fund Analytics project. It includes the column names, data types, business definitions, and source references for each table in the SQLite star schema.

---

# Dimension Tables

## 1. dim_fund

**Purpose:** Stores master information about every mutual fund scheme.

**Source:** `01_fund_master.csv`

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| amfi_code | INTEGER | Unique AMFI code identifying each mutual fund scheme. Used as the primary key and for joining datasets. | 01_fund_master.csv |
| scheme_name | TEXT | Name of the mutual fund scheme. | 01_fund_master.csv |
| fund_house | TEXT | Asset Management Company (AMC) managing the scheme. | 01_fund_master.csv |
| category | TEXT | Broad mutual fund category (Equity, Debt, Hybrid, etc.). | 01_fund_master.csv |
| sub_category | TEXT | Detailed category of the scheme. | 01_fund_master.csv |
| plan | TEXT | Investment plan type (Direct/Regular). | 01_fund_master.csv |
| launch_date | DATE | Date on which the scheme was launched. | 01_fund_master.csv |
| benchmark | TEXT | Benchmark index used to compare scheme performance. | 01_fund_master.csv |
| risk_category | TEXT | Risk level assigned to the mutual fund. | 01_fund_master.csv |

---

## 2. dim_date

**Purpose:** Stores calendar information for time-based analysis.

**Source:** Generated from `02_nav_history_cleaned.csv`

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| date_id | INTEGER | Unique identifier for each date. | Generated |
| full_date | DATE | Calendar date. | 02_nav_history_cleaned.csv |
| day | INTEGER | Day of the month. | Generated |
| month | INTEGER | Month number (1–12). | Generated |
| month_name | TEXT | Name of the month. | Generated |
| quarter | INTEGER | Quarter of the year (1–4). | Generated |
| year | INTEGER | Calendar year. | Generated |
| weekday | TEXT | Day of the week. | Generated |

---

# Fact Tables

## 3. fact_nav

**Purpose:** Stores historical Net Asset Value (NAV) records for each mutual fund.

**Source:** `02_nav_history.csv`

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| amfi_code | INTEGER | Mutual fund scheme identifier. | 02_nav_history.csv |
| date | DATE | Date on which NAV was recorded. | 02_nav_history.csv |
| nav | REAL | Net Asset Value of the scheme on the specified date. | 02_nav_history.csv |

---

## 4. fact_transactions

**Purpose:** Stores investor transaction records.

**Source:** `08_investor_transactions.csv`

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| investor_id | TEXT | Unique identifier for an investor. | 08_investor_transactions.csv |
| transaction_date | DATE | Date of the transaction. | 08_investor_transactions.csv |
| amfi_code | INTEGER | Mutual fund scheme involved in the transaction. | 08_investor_transactions.csv |
| transaction_type | TEXT | Type of transaction (SIP, Lumpsum, Redemption). | 08_investor_transactions.csv |
| amount_inr | REAL | Transaction amount in Indian Rupees. | 08_investor_transactions.csv |
| state | TEXT | State of the investor. | 08_investor_transactions.csv |
| city | TEXT | City of the investor. | 08_investor_transactions.csv |
| city_tier | TEXT | Classification of the city (Tier 1, Tier 2, Tier 3). | 08_investor_transactions.csv |
| age_group | TEXT | Investor age group. | 08_investor_transactions.csv |
| gender | TEXT | Gender of the investor. | 08_investor_transactions.csv |
| annual_income_lakh | REAL | Annual income of the investor (in lakh INR). | 08_investor_transactions.csv |
| payment_mode | TEXT | Payment method used for the transaction. | 08_investor_transactions.csv |
| kyc_status | TEXT | Investor KYC verification status. | 08_investor_transactions.csv |

---

## 5. fact_performance

**Purpose:** Stores key performance metrics of mutual fund schemes.

**Source:** `07_scheme_performance.csv`

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| amfi_code | INTEGER | Mutual fund scheme identifier. | 07_scheme_performance.csv |
| return_1yr_pct | REAL | One-year annualized return (%). | 07_scheme_performance.csv |
| return_3yr_pct | REAL | Three-year annualized return (%). | 07_scheme_performance.csv |
| return_5yr_pct | REAL | Five-year annualized return (%). | 07_scheme_performance.csv |
| benchmark_3yr_pct | REAL | Three-year benchmark return (%). | 07_scheme_performance.csv |
| alpha | REAL | Alpha performance metric. | 07_scheme_performance.csv |
| beta | REAL | Beta (market sensitivity). | 07_scheme_performance.csv |
| sharpe_ratio | REAL | Risk-adjusted return measured using Sharpe Ratio. | 07_scheme_performance.csv |
| sortino_ratio | REAL | Downside risk-adjusted return. | 07_scheme_performance.csv |
| std_dev_ann_pct | REAL | Annualized standard deviation of returns (%). | 07_scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum observed loss from peak to trough (%). | 07_scheme_performance.csv |
| aum_crore | REAL | Assets Under Management (₹ Crore). | 07_scheme_performance.csv |
| expense_ratio_pct | REAL | Annual expense ratio charged by the fund (%). | 07_scheme_performance.csv |
| morningstar_rating | INTEGER | Morningstar rating assigned to the scheme. | 07_scheme_performance.csv |
| risk_grade | TEXT | Overall risk grade assigned to the fund. | 07_scheme_performance.csv |

---

## 6. fact_aum

**Purpose:** Stores Assets Under Management (AUM) statistics for fund houses.

**Source:** `03_aum_by_fund_house.csv`

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| report_date | DATE | Reporting month/date of the AUM record. | 03_aum_by_fund_house.csv |
| fund_house | TEXT | Name of the Asset Management Company. | 03_aum_by_fund_house.csv |
| aum_lakh_crore | REAL | Total Assets Under Management in lakh crore INR. | 03_aum_by_fund_house.csv |
| aum_crore | REAL | Total Assets Under Management in crore INR. | 03_aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of mutual fund schemes managed by the AMC. | 03_aum_by_fund_house.csv |

---

# Notes

- All cleaned datasets are stored in the `data/processed/` directory.
- Date fields were converted to `datetime` format during preprocessing.
- Duplicate records were removed wherever applicable.
- Business validation checks were performed on NAV values, transaction amounts, expense ratios, and categorical fields before loading the data into SQLite.