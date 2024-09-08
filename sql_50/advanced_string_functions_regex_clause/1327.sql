SELECT
    p.product_name,
    SUM(o.unit) as unit
FROM
    Orders o
    JOIN Products p ON o.product_id = p.product_id
WHERE
    MONTH (order_date) = 2
    and YEAR (order_date) = 2020
GROUP BY
    o.product_id
HAVING
    unit >= 100