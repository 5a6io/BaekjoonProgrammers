select ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, "%Y-%m-%d") as OUT_DATE,
case
    when year(OUT_DATE) < 2022 or (year(OUT_DATE) = 2022 and month(OUT_DATE) < 5) or (year(OUT_DATE) = 2022 and month(OUT_DATE) = 5 and day(OUT_DATE) = 1)
    then '출고완료'
    when OUT_DATE is null
    then '출고미정'
    else '출고대기'
end as '출고여부'
from FOOD_ORDER 
order by ORDER_ID