SELECT s.id as id, COALESCE(s2.student, s.student) as student
FROM Seat s
LEFT JOIN Seat s2 on s.id = s2.id - 1
WHERE s.id % 2 = 1
UNION
SELECT s.id as id, s2.student as student
FROM Seat s
LEFT JOIN Seat s2 on s.id - 1 = s2.id
WHERE s.id % 2 = 0
ORDER BY id;