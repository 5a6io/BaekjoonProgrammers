select user_id, nickname, concat(city, ' ',street_address1, ' ', street_address2) as '전체주소', insert(insert(tlno, 4, 0,'-'), 9, 0, '-') as '전화번호'
from used_goods_user
where user_id in (select writer_id
                  from used_goods_board
                  group by writer_id
                  having count(board_id) >= 3)
order by user_id desc