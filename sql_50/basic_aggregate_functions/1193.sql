select
    DATE_FORMAT (trans_date, '%Y-%m') as month,
    country,
    COUNT(*) as trans_count,
    SUM(state = "approved") as approved_count,
    SUM(amount) as trans_total_amount,
    SUM((state = "approved") * amount) as approved_total_amount
from
    Transactions
group by
    month,
    country;