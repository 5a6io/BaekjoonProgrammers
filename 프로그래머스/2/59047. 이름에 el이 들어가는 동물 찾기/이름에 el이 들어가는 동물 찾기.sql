select animal_id, name
from animal_ins
where upper(name) like '%EL%' and animal_type = 'Dog'
order by name