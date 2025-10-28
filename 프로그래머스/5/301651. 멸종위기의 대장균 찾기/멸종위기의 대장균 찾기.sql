with recursive generation as (
    select id, parent_id, 1 as generation
    from ecoli_data
    where parent_id is null
    
    union all
    
    select e.id, e.parent_id, generation+1 as generation
    from ecoli_data e
    join generation g on e.parent_id = g.id
)

select count(*) as count, generation
from generation
where id not in (select distinct(parent_id) from generation where parent_id is not null)
group by generation
order by generation