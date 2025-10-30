select apnt_no, pt_name, a.pt_no, a.mcdp_cd, dr_name, apnt_ymd
from appointment a join doctor d on a.mddr_id = d.dr_id join patient p on p.pt_no = a.pt_no
where date_format(apnt_ymd, '%Y-%m-%d') = '2022-04-13' and apnt_cncl_yn = 'N'
order by apnt_ymd