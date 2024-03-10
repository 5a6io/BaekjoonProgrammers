select O.ANIMAL_ID, ANIMAL_TYPE, NAME
from ANIMAL_OUTS O join (select ANIMAL_ID
                    from ANIMAL_INS
                    where SEX_UPON_INTAKE like 'Intact%') I on O.ANIMAL_ID = I.ANIMAL_ID
where SEX_UPON_OUTCOME like 'Neutered%' or SEX_UPON_OUTCOME like 'Spayed%'
order by O.ANIMAL_ID