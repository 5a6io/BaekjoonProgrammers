with developers as(
    select (case
       when skill_code&(select code
                       from skillcodes
                       where name='Python') and skill_code&(select sum(code)
                                                           from skillcodes
                                                           where category='Front End') then 'A'
       when skill_code&(select code
                       from skillcodes
                       where name='C#') then 'B'
       when skill_code&(select sum(code)
                                    from skillcodes
                                    where category='Front End') then 'C' end) as grade, id, email
    from developers
)

select *
from developers
where grade is not null
order by grade, id