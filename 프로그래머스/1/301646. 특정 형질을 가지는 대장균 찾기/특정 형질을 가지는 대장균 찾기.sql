select count(id) as count
from ecoli_data
where (genotype & 1 or genotype & 4) and ~genotype & 2