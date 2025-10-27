with history as (
    select history_id, car_type, datediff(end_date, start_date) + 1 as duration,
    case
        when datediff(end_date, start_date) + 1 >= 90 then '90일 이상'
        when datediff(end_date, start_date) + 1 >= 30 then '30일 이상'
        when datediff(end_date, start_date) + 1 >= 7 then '7일 이상'
        else null end as duration_type, daily_fee
    from car_rental_company_rental_history h join car_rental_company_car c on h.car_id = c.car_id
)

select history_id, round(duration * daily_fee * (100 - ifnull(discount_rate, 0)) / 100) as fee
from history h left join car_rental_company_discount_plan p on h.car_type = p.car_type and h.duration_type = p.duration_type
where h.car_type = '트럭'
order by fee desc, history_id desc