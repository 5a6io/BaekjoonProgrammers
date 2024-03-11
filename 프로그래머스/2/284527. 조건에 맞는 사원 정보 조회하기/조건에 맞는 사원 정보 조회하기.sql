select SCORE, E.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES E join (select EMP_NO, sum(SCORE) as SCORE
                         from HR_GRADE
                         group by EMP_NO) G on E.EMP_NO = G.EMP_NO
order by SCORE desc limit 1