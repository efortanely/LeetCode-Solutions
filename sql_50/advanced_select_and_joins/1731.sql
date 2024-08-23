SELECT
    manager.employee_id,
    manager.name,
    COUNT(*) as reports_count,
    ROUND(AVG(employee.age)) as average_age
FROM
    Employees as manager
    CROSS JOIN Employees as employee on employee.reports_to = manager.employee_id
GROUP BY
    manager.employee_id
ORDER BY
    manager.employee_id;