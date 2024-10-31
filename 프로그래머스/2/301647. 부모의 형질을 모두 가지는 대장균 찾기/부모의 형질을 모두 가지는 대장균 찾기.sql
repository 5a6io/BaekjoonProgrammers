select a.id, a.genotype, b.genotype as parent_genotype
from ecoli_data a join ecoli_data b on a.parent_id = b.id
where b.genotype&a.genotype = b.genotype
order by a.id