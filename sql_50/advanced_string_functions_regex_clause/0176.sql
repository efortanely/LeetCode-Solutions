WITH
    salaries AS (
        SELECT
            id,
            salary,
            DENSE_RANK() OVER (
                ORDER BY
                    salary DESC
            ) AS salary_rank
        FROM
            Employee
    )
SELECT
    CASE
        WHEN COUNT(*) < 2 THEN NULL
        ELSE MAX(
            CASE
                WHEN salary_rank = 2 THEN salary
            END
        )
    END AS SecondHighestSalary
FROM
    salaries;