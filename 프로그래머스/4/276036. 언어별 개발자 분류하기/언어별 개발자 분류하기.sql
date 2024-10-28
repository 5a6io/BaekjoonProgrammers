with FRONT as (
    select BIT_OR(CODE) as SKILL_CODE
    from SKILLCODES
    group by CATEGORY
    having CATEGORY = 'Front End'
), DEV as (
    select
        case
            when D.SKILL_CODE & F.SKILL_CODE
                and D.SKILL_CODE & (select CODE from SKILLCODES where NAME = 'Python') then 'A'
            when D.SKILL_CODE & (select CODE from SKILLCODES where NAME = 'C#') then 'B'
            when D.SKILL_CODE & F.SKILL_CODE then 'C'
            else NULL
        end as GRADE, ID, EMAIL
    from DEVELOPERS D, FRONT F)

select GRADE, ID, EMAIL
from DEV
where GRADE IS NOT NULL
order by GRADE, ID