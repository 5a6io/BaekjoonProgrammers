select ID, ifnull(CHILD_COUNT, 0) as CHILD_COUNT
from ECOLI_DATA A left outer join (select PARENT_ID, count(ID) as CHILD_COUNT
                       from ECOLI_DATA
                       group by PARENT_ID) B on A.ID = B.PARENT_ID
order by ID