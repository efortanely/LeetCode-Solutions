WITH
    max_friends AS (
        SELECT
            *,
            COUNT(id_table.id) as id_count
        FROM
            (
                SELECT DISTINCT
                    requester_id AS id
                FROM
                    RequestAccepted
                UNION
                SELECT DISTINCT
                    accepter_id AS id
                FROM
                    RequestAccepted
            ) AS id_table
            JOIN RequestAccepted ra ON id_table.id = requester_id
            OR id_table.id = accepter_id
        GROUP BY
            id_table.id
        ORDER BY
            id_count DESC
        LIMIT
            1
    )
SELECT
    id,
    id_count as num
FROM
    max_friends