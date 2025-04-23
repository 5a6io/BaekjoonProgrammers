select distinct(c.car_id) as "car_id"
from car_rental_company_rental_history h left outer join car_rental_company_car c on h.car_id = c.car_id
where car_type = "세단" and month(start_date) = 10
order by c.car_id desc