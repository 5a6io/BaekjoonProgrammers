select id, case
                when size_rank <= 0.25 then 'CRITICAL'
                when size_rank <= 0.50 then 'HIGH'
                when size_rank <= 0.75 then 'MEDIUM'
                else 'LOW'
            end as colony_name
from (select id, percent_rank() over (order by size_of_colony desc) as size_rank
     from ecoli_data) ed
order by id