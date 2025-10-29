select p.product_id, product_name, price * sum(amount) as total_sales
from food_product p left join food_order o on p.product_id = o.product_id
where year(produce_date) = 2022 and month(produce_date) = 5
group by o.product_id
order by total_sales desc, p.product_id