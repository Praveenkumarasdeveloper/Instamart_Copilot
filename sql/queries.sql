-- Instamart project: SQL queries used in Part A
-- Source: original SQL_Database_part_a.ipynb
-- Required SQLite tables: customers, products, orders

-- Q1: Customers with qualifying completed spend
SELECT
        customer_id,
        ROUND(SUM(order_amount), 2) AS spend_over_500
    FROM orders
    WHERE status = 'completed'
      AND order_amount > 500
    GROUP BY customer_id
    HAVING SUM(order_amount) > 8000
    ORDER BY spend_over_500 DESC;

-- Q2: Revenue by city and product category
SELECT
        c.city,
        p.category,
        ROUND(SUM(o.order_amount), 2) AS revenue
    FROM orders AS o
    JOIN customers AS c
        ON o.customer_id = c.customer_id
    JOIN products AS p
        ON o.product_id = p.product_id
    WHERE o.status = 'completed'
    GROUP BY c.city, p.category
    ORDER BY c.city, p.category;

-- Q3: Products priced above the average
SELECT
        product_id,
        product_name,
        price_inr
    FROM products
    WHERE price_inr > (
        SELECT AVG(price_inr)
        FROM products
    )
    ORDER BY price_inr DESC;

-- Q4: Customers without completed orders
SELECT
        c.customer_id
    FROM customers AS c
    LEFT JOIN orders AS o
        ON c.customer_id = o.customer_id
        AND o.status = 'completed'
    WHERE o.order_id IS NULL
    ORDER BY c.customer_id;

-- Q5: Customers spending above the customer average
WITH customer_spend AS (
        SELECT
            customer_id,
            SUM(order_amount) AS total_spend
        FROM orders
        WHERE status = 'completed'
        GROUP BY customer_id
    ),
    average_spend AS (
        SELECT
            AVG(total_spend) AS avg_spend
        FROM customer_spend
    )
    SELECT
        customer_id,
        ROUND(total_spend, 2) AS total_spend
    FROM customer_spend
    CROSS JOIN average_spend
    WHERE total_spend > avg_spend
    ORDER BY total_spend DESC;

-- Q6: Customer spending ranks within each city
WITH spend AS (
        SELECT
            c.customer_id,
            c.city,
            SUM(o.order_amount) AS total_spend
        FROM customers AS c
        JOIN orders AS o
            ON c.customer_id = o.customer_id
        WHERE o.status = 'completed'
        GROUP BY c.customer_id, c.city
    )
    SELECT
        customer_id,
        city,
        ROUND(total_spend, 2) AS total_spend,

        RANK() OVER (
            PARTITION BY city
            ORDER BY total_spend DESC
        ) AS spend_rank,

        DENSE_RANK() OVER (
            PARTITION BY city
            ORDER BY total_spend DESC
        ) AS dense_rank,

        ROW_NUMBER() OVER (
            PARTITION BY city
            ORDER BY total_spend DESC, customer_id
        ) AS row_num

    FROM spend
    ORDER BY city, spend_rank, customer_id;

-- Q7: Daily revenue and cumulative running total
WITH daily AS (
        SELECT
            substr(order_ts, 1, 10) AS day,
            SUM(order_amount) AS revenue
        FROM orders
        WHERE status = 'completed'
        GROUP BY substr(order_ts, 1, 10)
    )
    SELECT
        day,
        ROUND(revenue, 2) AS revenue,
        ROUND(
            SUM(revenue) OVER (
                ORDER BY day
                ROWS BETWEEN UNBOUNDED PRECEDING
                AND CURRENT ROW
            ),
            2
        ) AS cumulative_revenue
    FROM daily
    ORDER BY day;

