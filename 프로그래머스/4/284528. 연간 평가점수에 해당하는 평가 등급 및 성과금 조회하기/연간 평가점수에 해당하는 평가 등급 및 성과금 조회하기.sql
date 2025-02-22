select e.emp_no, emp_name, case when avg(score) >= 96 then "S"
    when avg(score) >= 90 then "A"
    when avg(score) >= 80 then "B"
    else "C" end as grade, case when avg(score) >= 96 then sal * 0.2
    when avg(score) >= 90 then sal * 0.15
    when avg(score) >= 80 then sal * 0.1
    else 0 end as bonus
from hr_employees e join hr_grade g on e.emp_no = g.emp_no
group by e.emp_no
order by e.emp_no