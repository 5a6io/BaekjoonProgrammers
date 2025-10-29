# 서브쿼리를 이용한 풀이
# select animal_id, animal_type, name
# from animal_outs
# where animal_id in (select animal_id
#                        from animal_ins
#                        where sex_upon_intake like 'Intact%') and
#                        (sex_upon_outcome like 'Spayed%' or sex_upon_outcome like 'Neutered%')

# join을 이용한 풀이
select o.animal_id, o.animal_type, o.name
from animal_outs o inner join animal_ins i on o.animal_id = i.animal_id
where sex_upon_intake like 'Intact%' and sex_upon_outcome not like 'Intact%'