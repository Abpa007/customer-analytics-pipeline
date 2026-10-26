-- 1. Find the top 5 countries/regions with the most customers
SELECT country, COUNT(*) AS total_customers 
FROM customers 
GROUP BY country 
ORDER BY total_customers DESC 
LIMIT 5;

-- 2. Customer Distribution by Industry or Segment (Adjust column name based on your CSV)
SELECT industry, COUNT(*) AS customer_count
FROM customers
GROUP BY industry
ORDER BY customer_count DESC;

-- 3. Summary metrics: Total customer base size
SELECT COUNT(*) AS overall_customer_count FROM customers;