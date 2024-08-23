select
    query_name,
    ROUND(AVG(rating / position), 2) as quality,
    ROUND(
        SUM(
            CASE
                WHEN rating < 3 THEN 1
                ELSE 0
            END
        ) * 100 / COUNT(*),
        2
    ) as poor_query_percentage
from
    Queries
where
    query_name is not null
group by
    query_name;