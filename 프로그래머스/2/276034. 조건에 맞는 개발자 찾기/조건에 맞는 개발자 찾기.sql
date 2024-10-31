select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where SKILL_CODE & (select bit_or(CODE)
                   from SKILLCODES
                   where NAME = 'Python' or NAME = 'C#')
order by ID