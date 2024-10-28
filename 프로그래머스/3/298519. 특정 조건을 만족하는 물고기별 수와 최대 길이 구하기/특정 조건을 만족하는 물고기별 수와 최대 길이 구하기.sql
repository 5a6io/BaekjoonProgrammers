select count(FISH_TYPE) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE 
from FISH_INFO
group by FISH_TYPE
having avg(IF(LENGTH IS NULL, 10, LENGTH)) >= 33
order by FISH_TYPE