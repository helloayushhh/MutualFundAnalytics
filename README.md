# mutual fund analytics

an end-to-end data analytics project built using python, sql, sqlite, and power bi to process mutual fund datasets, perform data cleaning and validation, design a star schema database, execute analytical sql queries, and build an interactive dashboard.

---

## tech stack

- python
- pandas
- sqlite
- sql
- power bi
- git

---

## project structure

```text
mutual-fund-analytics
│
├── data
│   ├── raw
│   └── processed
│
├── scripts
│   ├── data_cleaning.py
│   ├── load_sqlite.py
│   └── ...
│
├── sql
│   ├── schema.sql
│   └── queries.sql
│
├── reports
│   ├── data_dictionary.md
│   └── dashboard.pbix
│
└── readme.md
```

---

## features

### data cleaning

- parsed and standardized date columns
- removed duplicate records
- validated missing values
- standardized transaction types
- validated nav, aum, returns, expense ratio, and kyc values
- generated cleaned datasets

### database

designed and implemented a sqlite star schema including:

- dim_fund
- dim_date
- fact_nav
- fact_transactions
- fact_performance
- fact_aum

### sql analytics

implemented analytical sql queries including:

- top funds by aum
- average monthly nav
- transactions by state
- expense ratio analysis
- sip growth analysis
- fund performance insights

### dashboard

power bi dashboard includes:

- nav trends
- aum analysis
- fund performance
- investor transaction insights
- kpi cards
- interactive filters

---

## workflow

```text
raw csv files
      │
      ▼
python data cleaning
      │
      ▼
processed csv files
      │
      ▼
sqlite database
      │
      ▼
sql analytics
      │
      ▼
power bi dashboard
```

---

## dataset summary

| dataset | records |
|---------|--------:|
| nav history | 46,000 |
| investor transactions | 32,778 |
| scheme performance | 40 |
| fund master | 40 |
| aum by fund house | 90 |

---

## running locally

clone the repository

```bash
git clone https://github.com/helloayushhh/mutual-fund-analytics.git
```

install dependencies

```bash
pip install -r requirements.txt
```

run data cleaning

```bash
python scripts/data_cleaning.py
```

load sqlite database

```bash
python scripts/load_sqlite.py
```

---

## current progress

- ✅ data cleaning
- ✅ data validation
- ✅ sqlite database
- ✅ star schema design
- ✅ sql queries
- ✅ data dictionary
- 🚧 power bi dashboard

---

## author

github: https://github.com/helloayushhh

see you in the next build
---aps
