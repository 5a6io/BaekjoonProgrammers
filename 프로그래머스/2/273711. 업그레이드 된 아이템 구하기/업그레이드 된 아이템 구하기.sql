select ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO
where ITEM_ID in (select T.ITEM_ID
                 from ITEM_TREE T join ITEM_INFO I on T.PARENT_ITEM_ID = I.ITEM_ID
                 where RARITY = 'RARE')
order by ITEM_ID desc