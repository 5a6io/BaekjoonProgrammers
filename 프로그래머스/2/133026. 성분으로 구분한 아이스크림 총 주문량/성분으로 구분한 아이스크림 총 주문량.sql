select INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from ICECREAM_INFO I join (select *
                        from FIRST_HALF
                        group by FLAVOR) F on F.FLAVOR = I.FLAVOR
group by INGREDIENT_TYPE