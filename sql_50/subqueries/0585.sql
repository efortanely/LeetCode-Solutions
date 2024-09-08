WITH
    i3 AS (
        SELECT
            i1.pid,
            i1.tiv_2015,
            i1.tiv_2016
        FROM
            Insurance i1
            JOIN Insurance i2 ON i1.tiv_2015 = i2.tiv_2015
            AND i1.pid != i2.pid
        WHERE
            (i1.lat, i1.lon) IN (
                SELECT
                    lat,
                    lon
                FROM
                    Insurance
                GROUP BY
                    lat,
                    lon
                HAVING
                    COUNT(*) = 1
            )
    )
SELECT
    ROUND(SUM(tiv_2016), 2) as tiv_2016
FROM
    (
        SELECT DISTINCT
            (pid),
            tiv_2016
        FROM
            i3
    ) AS i4