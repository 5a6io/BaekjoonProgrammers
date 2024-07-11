select APNT_NO, PT_NAME, A.PT_NO, MCDP_CD, DR_NAME, APNT_YMD
from APPOINTMENT A inner join PATIENT P on A.PT_NO = P.PT_NO left join (select DR_NAME, DR_ID
 from DOCTOR) D on MDDR_ID = D.DR_ID
 where DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13' and APNT_CNCL_YN = 'N' and MCDP_CD = 'CS'
order by APNT_YMD