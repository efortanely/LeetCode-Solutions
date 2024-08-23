SELECT DISTINCT
    l1.num as ConsecutiveNums
FROM
    Logs l1
    JOIN Logs l2 ON l1.id + 1 = l2.id
    JOIN Logs l3 on l2.id + 1 = l3.id
WHERE
    l1.num = l2.num
    AND l2.num = l3.num;