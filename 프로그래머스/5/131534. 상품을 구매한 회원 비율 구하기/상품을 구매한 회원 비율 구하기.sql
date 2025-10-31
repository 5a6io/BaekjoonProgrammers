select year(sales_date) as year, month(sales_date) as month, count(distinct s.user_id) as purchased_users, round(count(distinct s.user_id) / (select count(*) from user_info where year(joined)=2021), 1) as puchased_ratio
from user_info i join online_sale s on i.user_id = s.user_id
where year(joined) = 2021
group by year, month
order by year, month