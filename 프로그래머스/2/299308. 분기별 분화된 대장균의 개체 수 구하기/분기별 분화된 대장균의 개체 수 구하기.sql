with ecoli_quarter as(
    select id, (case
       when month(differentiation_date) < 4 then 1
       when month(differentiation_date) < 7 then 2
       when month(differentiation_date) < 10 then 3
       else 4 end) as quarter
    from ecoli_data
)

select concat(quarter, 'Q') as quarter, count(id) as ecoli_count
from ecoli_quarter
group by quarter
order by quarter