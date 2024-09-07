# Write your MySQL query statement below
SELECT
    q.person_name
FROM
    (SELECT 
        q1.person_id,
        q1.person_name,
        q1.weight + COALESCE(SUM(q2.weight), 0) as total_weight,
        q1.turn
    FROM Queue q1
    LEFT JOIN Queue q2 ON q1.turn > q2.turn
    GROUP BY q1.person_id
    HAVING total_weight <= 1000) as q
ORDER BY q.turn DESC LIMIT 1;