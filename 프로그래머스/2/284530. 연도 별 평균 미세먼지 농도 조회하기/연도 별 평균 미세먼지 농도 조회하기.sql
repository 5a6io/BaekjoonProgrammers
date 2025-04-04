select year(ym) as 'year', round(avg(pm_val1), 2) as 'pm10', round(avg(pm_val2), 2) as 'pm2.5'
from air_pollution
group by location2, location1, year(ym)
having location2 = '수원'
order by year