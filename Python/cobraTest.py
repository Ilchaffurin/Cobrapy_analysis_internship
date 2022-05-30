# -*- coding: utf-8 -*-
#conda env = Cobrapy
import cobra.test
import os
from os.path import join

data_dir = cobra.test.data_dir

print("mini test files: ")
print(", ".join(i for i in os.listdir(data_dir) if i.startswith("mini")))

textbook_model = cobra.test.create_test_model("textbook")
#ecoli_model = cobra.test.create_test_model("ecoli")
#salmonella_model = cobra.test.create_test_model("salmonella")
""" POUR PRINT TOUTES LES REACTIONS ET TOUT LES METABOLITES (+leurs gènes)
for reaction in ecoli_model.reactions:
	print(str(reaction.id)+str(reaction.reaction))

for x in ecoli_model.genes:
    associated_ids = (i.id for i in x.reactions)
    print("%s is associated with reactions: %s" %
          (x.id, "{" + ", ".join(associated_ids) + "}"))"""

print(textbook_model.summary())
solution=textbook_model.optimize()
print("###SOLUTION###")
print(solution.objective_value)
print(solution.status)
print(solution.fluxes)