-- LABEL ALL ROWS AFTER DATE AS 10, REMOVE THE ROWS THAT ARE AFTER THE DATE
SELECT
    product_id,
    CASE
        WHEN change_date <= "2019-08-16" THEN new_price
        ELSE 10
    END AS price
FROM
    Products
HAVING
    (product_id) NOT IN (
        SELECT
            product_id
        FROM
            Products
        WHERE
            change_date <= "2019-08-16"
    )
UNION
-- GET THE MAX DATE PRIOR TO THE DATE FOR EACH PRODUCT ID
SELECT
    p.product_id,
    p.new_price as price
FROM
    Products p
    JOIN (
        SELECT
            product_id,
            MAX(change_date) AS max_change_date
        FROM
            Products
        WHERE
            change_date <= "2019-08-16"
        GROUP BY
            product_id
    ) AS b ON p.product_id = b.product_id
    AND p.change_date = b.max_change_date;