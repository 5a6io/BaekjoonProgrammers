with average as (
    select year(differentiation_date) as year, max(size_of_colony) as max
    from ecoli_data
    group by year(differentiation_date)
)

select e.year, (max - size_of_colony) as year_dev, id
from (select year(differentiation_date) as year, size_of_colony, id
     from ecoli_data) e join average a on e.year = a.year
order by year, year_dev