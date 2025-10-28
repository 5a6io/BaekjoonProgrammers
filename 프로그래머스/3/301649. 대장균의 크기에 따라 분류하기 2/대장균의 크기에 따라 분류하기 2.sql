with ranking as (
    select id, percent_rank() over (order by size_of_colony desc) as ranking
    from ecoli_data
)

select id, (case
            when ranking <= 0.25 then 'CRITICAL'
            when ranking <= 0.5 then 'HIGH'
            when ranking <= 0.75 then 'MEDIUM'
            else 'LOW' end) as colony_name
from ranking
order by id