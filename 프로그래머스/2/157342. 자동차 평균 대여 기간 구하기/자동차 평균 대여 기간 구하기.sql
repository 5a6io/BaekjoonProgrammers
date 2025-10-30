select car_id, round(avg(duration), 1) as average_duration
from (select car_id, datediff(end_date, start_date)+1 as duration
      from car_rental_company_rental_history) a
group by car_id
having avg(duration) >= 7
order by average_duration desc, car_id desc