select distinct CAR_ID, C.CAR_TYPE, round(DAILY_FEE*30*(100-DISCOUNT_RATE)/100) as FEE
from CAR_RENTAL_COMPANY_CAR C join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P on C.CAR_TYPE = P.CAR_TYPE
where C.CAR_TYPE in ('세단','SUV') and CAR_ID not in (select CAR_ID
                    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                    where '2022-11' between date_format(START_DATE, "%Y-%m") and date_format(END_DATE, "%Y-%m"))
      and DURATION_TYPE like '30%' and DAILY_FEE*30*(100-DISCOUNT_RATE)/100 between 500000 and 2000000
order by FEE desc, C.CAR_TYPE, CAR_ID desc