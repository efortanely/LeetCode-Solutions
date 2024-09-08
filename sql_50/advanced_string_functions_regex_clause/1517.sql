SELECT
    *
FROM
    Users
WHERE
    mail REGEXP '^[A-Za-z][a-zA-Z0-9_.-]*\\@leetcode\\.com$'