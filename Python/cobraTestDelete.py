# -*- coding: utf-8 -*-
#conda env = Cobrapy

import pandas
from time import time

import cobra.test
from cobra.flux_analysis import (
    single_gene_deletion, single_reaction_deletion, double_gene_deletion,
    double_reaction_deletion)

cobra_model = cobra.test.create_test_model("textbook")
ecoli_model = cobra.test.create_test_model("ecoli")

print(ecoli_model.summary())
print('complete model: ', cobra_model.optimize())
with cobra_model:
    cobra_model.reactions.PFK.knock_out()
    print('pfk knocked out: ', cobra_model.optimize())

for reaction in ecoli_model.reactions:
	print(str(reaction.id)+str(reaction.reaction))
