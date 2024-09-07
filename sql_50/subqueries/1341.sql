SELECT
    name as results
FROM
    (
        SELECT
            mr.user_id,
            COUNT(mr.user_id) as max_ratings
        FROM
            MovieRating mr
            JOIN Users u2 on mr.user_id = u2.user_id
        GROUP BY
            user_id
        ORDER BY
            max_ratings DESC,
            u2.name
        LIMIT
            1
    ) r
    JOIN Users u ON u.user_id = r.user_id
UNION ALL
SELECT
    ra.title as results
FROM
    (
        SELECT
            m.title,
            AVG(rating) as average_rating
        FROM
            MovieRating mr
            JOIN Movies m ON mr.movie_id = m.movie_id
        WHERE
            MONTH (mr.created_at) = 2
            AND YEAR (mr.created_at) = 2020
        GROUP BY
            mr.movie_id
        ORDER BY
            average_rating DESC,
            m.title
        LIMIT
            1
    ) ra
    JOIN Movies m ON ra.title = m.title;