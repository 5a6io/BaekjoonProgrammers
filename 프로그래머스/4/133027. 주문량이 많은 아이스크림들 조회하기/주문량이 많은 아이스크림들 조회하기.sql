select F.FLAVOR
from FIRST_HALF F join (select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
                       from JULY
                       group by FLAVOR) J on F.FLAVOR = J.FLAVOR
group by F.FLAVOR
order by sum(F.TOTAL_ORDER) + sum(J.TOTAL_ORDER) desc limit 3