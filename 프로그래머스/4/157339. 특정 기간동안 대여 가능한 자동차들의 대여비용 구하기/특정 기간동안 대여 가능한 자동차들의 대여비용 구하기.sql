select car_id, c.car_type, round(30*daily_fee*(100-discount_rate) / 100) as fee
from car_rental_company_car c left join (select car_type, discount_rate
                                      from car_rental_company_discount_plan
                                      where duration_type = '30일 이상') r on c.car_type = r.car_type
where car_id not in (select car_id
                     from car_rental_company_rental_history
                     where '2022-11-01' <= end_date and start_date <= '2022-11-30') and (c.car_type = '세단' or c.car_type = 'SUV') and 500000 <= 30*daily_fee*(100-discount_rate) / 100 and 30*daily_fee*(100-discount_rate) / 100 < 2000000
order by fee desc, c.car_type, car_id desc