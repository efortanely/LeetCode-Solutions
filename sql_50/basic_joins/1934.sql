SELECT
    user_counts.user_id,
    ROUND(IFNULL (AVG(con / (con + tim)), 0), 2) as confirmation_rate
FROM
    (
        SELECT
            s.user_id,
            SUM(
                CASE
                    WHEN c.action = 'confirmed' THEN 1
                    ELSE 0
                END
            ) AS con,
            SUM(
                CASE
                    WHEN c.action = 'timeout' THEN 1
                    ELSE 0
                END
            ) AS tim
        FROM
            Signups s
            LEFT JOIN Confirmations c ON s.user_id = c.user_id
        GROUP BY
            s.user_id
    ) AS user_counts
GROUP BY
    user_counts.user_id
ORDER BY
    confirmation_rate;