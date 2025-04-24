select year(sales_date) as year, month(sales_date) as month, count(distinct(user_id)) as purchased_users, round(count(distinct(user_id))/(select count(user_id)
                 from user_info
                 where year(joined) = 2021), 1) as purchased_ratio
from online_sale
where user_id in (select user_id
                 from user_info
                 where year(joined) = 2021)
group by year(sales_date), month(sales_date)
order by year, month