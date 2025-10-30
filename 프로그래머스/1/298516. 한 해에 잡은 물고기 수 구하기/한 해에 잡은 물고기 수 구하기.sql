select count(id) as fish_count
from fish_info
where year(time) = 2021
group by year(time)