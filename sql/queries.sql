SELECT scheme_name, aum_crore
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;

SELECT amfi_code,
AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code;

SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

SELECT transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
WHERE expense_ratio_pct < 1;

SELECT AVG(return_3yr_pct) AS average_return_3yr
FROM fact_performance;

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

SELECT
kyc_status,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

SELECT
state,
SUM(amount_inr) AS investment
FROM fact_transactions
GROUP BY state
ORDER BY investment DESC
LIMIT 5;

SELECT
scheme_name,
morningstar_rating
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY morningstar_rating DESC
LIMIT 10;