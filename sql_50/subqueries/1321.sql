WITH
    v AS (
        SELECT DISTINCT
            c1.visited_on as visited_on
        FROM
            Customer c1
    )
SELECT
    v.visited_on,
    ROUND(SUM(c2.amount), 2) as amount,
    ROUND(SUM(c2.amount) / 7, 2) as average_amount
FROM
    v
    JOIN Customer c2 ON c2.visited_on BETWEEN DATE_SUB (v.visited_on, INTERVAL 6 DAY) AND v.visited_on
GROUP BY
    v.visited_on
HAVING
    COUNT(DISTINCT c2.visited_on) >= 7