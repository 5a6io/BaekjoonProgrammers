select CATEGORY, sum(SALES) as TOTAL_SALES
from BOOK B join BOOK_SALES S on B.BOOK_ID = S.BOOK_ID
where month(SALES_DATE) = 1
group by CATEGORY
order by CATEGORY