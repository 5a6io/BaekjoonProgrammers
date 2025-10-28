with recursive ecoli_gen as (
    select id, parent_id, 1 as gen
    from ecoli_data
    where parent_id is null
    
    union all
    
    select e.id, e.parent_id, gen + 1 as gen
    from ecoli_data e join ecoli_gen g on e.parent_id = g.id
)

select id
from ecoli_gen
where gen = 3
order by id