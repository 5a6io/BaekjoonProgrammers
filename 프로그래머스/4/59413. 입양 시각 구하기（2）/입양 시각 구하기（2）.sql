set @TIME := -1;

select (@TIME := @TIME+1) as TIME, (select count(*)
                                   from ANIMAL_OUTS
                                   where hour(DATETIME) = @TIME) as COUNT
from ANIMAL_OUTS
where @TIME < 23