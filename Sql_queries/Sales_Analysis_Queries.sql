
-- ==========================================
-- SALES ANALYTICS DASHBOARD
-- SQL DATA ANALYSIS QUERIES
-- ==========================================

USE sales_analytics;

-- 1. Total number of records
SELECT COUNT(*) AS total_records
FROM superstore_sales;


-- 2. Region-wise sales
SELECT
    region,
    SUM(sales) AS total_sales
FROM superstore_sales
GROUP BY region
ORDER BY total_sales DESC;


-- 3. Category-wise sales and profit
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM superstore_sales
GROUP BY category
ORDER BY total_sales DESC;


-- 4. Sales by customer segment
SELECT
    segment,
    SUM(sales) AS total_sales
FROM superstore_sales
GROUP BY segment
ORDER BY total_sales DESC;


-- 5. Top 10 states by sales
SELECT
    state,
    SUM(sales) AS total_sales
FROM superstore_sales
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;


-- 6. Top 10 sub-categories by profit
SELECT
    sub_category,
    SUM(profit) AS total_profit
FROM superstore_sales
GROUP BY sub_category
ORDER BY total_profit DESC
LIMIT 10;


-- 7. Loss-making sub-categories
SELECT
    sub_category,
    SUM(profit) AS total_profit
FROM superstore_sales
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;


-- 8. Monthly sales trend
SELECT
    YEAR(order_date) AS sales_year,
    MONTH(order_date) AS sales_month,
    SUM(sales) AS total_sales
FROM superstore_sales
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
ORDER BY
    sales_year,
    sales_month;
