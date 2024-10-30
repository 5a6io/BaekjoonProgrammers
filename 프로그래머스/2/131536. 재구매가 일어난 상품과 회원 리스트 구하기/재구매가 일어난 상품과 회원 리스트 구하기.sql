select distinct(USER_ID), PRODUCT_ID
from ONLINE_SALE A
where (USER_ID, PRODUCT_ID) in (select USER_ID, PRODUCT_ID
                               from ONLINE_SALE B
                               where A.SALES_DATE <> B.SALES_DATE)
order by USER_ID, PRODUCT_ID desc