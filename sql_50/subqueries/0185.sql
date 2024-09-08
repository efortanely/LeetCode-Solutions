WITH
    RankedSalaries AS (
        SELECT
            id,
            name,
            salary,
            departmentId,
            DENSE_RANK() OVER (
                PARTITION BY
                    departmentId
                ORDER BY
                    salary DESC
            ) AS salary_rank
        FROM
            Employee
    )
SELECT
    d.name as Department,
    rs.name as Employee,
    rs.salary as Salary
FROM
    RankedSalaries rs
    JOIN Department d ON rs.departmentId = d.id
WHERE
    salary_rank <= 3