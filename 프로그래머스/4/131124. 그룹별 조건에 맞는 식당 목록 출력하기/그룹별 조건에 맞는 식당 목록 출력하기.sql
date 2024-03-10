select MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE P join REST_REVIEW R on P.MEMBER_ID = R.MEMBER_ID
where P.MEMBER_ID = (select MEMBER_ID
                    from REST_REVIEW
                    group by MEMBER_ID
                    order by count(MEMBER_ID) desc limit 1)
order by REVIEW_DATE, REVIEW_TEXT