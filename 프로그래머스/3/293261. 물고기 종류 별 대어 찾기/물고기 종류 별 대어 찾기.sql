select ID, FISH_NAME, LENGTH
from FISH_INFO F inner join FISH_NAME_INFO N on F.FISH_TYPE = N.FISH_TYPE
where (F.FISH_TYPE, LENGTH) in (select FISH_TYPE, max(LENGTH)
                               from FISH_INFO
                               group by FISH_TYPE)
order by ID