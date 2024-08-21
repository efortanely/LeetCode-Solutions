SELECT
    name
FROM
    Employee
WHERE
    id in (
        SELECT
            managerId
        FROM
            Employee as e
        GROUP BY
            managerId
        HAVING
            COUNT(*) >= 5
    );