WITH
    UserCounts as (
        SELECT
            COUNT(*) as total_users
        FROM
            Users
    ),
    ContestUserCounts AS (
        SELECT
            r.contest_id,
            COUNT(r.user_id) as user_count
        FROM
            Register r
        GROUP BY
            r.contest_id
    )
SELECT
    c.contest_id,
    ROUND(100 * c.user_count / u.total_users, 2) as percentage
FROM
    ContestUserCounts c
    CROSS JOIN UserCounts u
ORDER BY
    percentage DESC,
    c.contest_id;