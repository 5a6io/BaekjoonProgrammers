select D.DEPT_ID, DEPT_NAME_EN, round(avg(SAL)) as AVG_SAL
from HR_EMPLOYEES E join HR_DEPARTMENT D on E.DEPT_ID = D.DEPT_ID
group by E.DEPT_ID
order by AVG_SAL desc