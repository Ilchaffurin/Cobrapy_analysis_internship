# Cobrapy_analysis_internship
Le travail fait lors de ce stage à été effectué à l'aide d'environnement [CONDA](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
## Installation
Il faut tout d'abord installer l'environnement CONDA à l'aide du fichier Cobrapy_environnement.yml.

```bash
conda env create -f environment.yml
```
Package notables : numpy,matplotlib,seaborn,pandas

## Utils_cobrapy.py
Ce fichier contient un module python permettant de facilier la manipulation et l'analyse des modèles COBRA utilisés lors de ce stage.
#### get_sum_fluxes()
fonction prenant en entrée un objet métabolite d'un modèle ayant déja effectué une FBA.
Renvoi la somme des flux produisant ce métabolite
#### get_fluxes_from_mitocore_metabolite()
fonction qui a partir d'un métabolite et d'un modèle, récupère tout les flux producteurs du métabolite, et
fais la somme des flux par sous système du modèle.
Renvoi un dictionnaire ayant pour clé les sous système et pour valeur la somme des flux de chaque sous système
#### get_mitocore_respiratory_exchange_ratio()
Permet de calculer le quotient respiratoire d'un modèle basé sur le modèle MitoCore.
#### define_boundary_and_run_model()
fonction qui applique une FBA sur un modèle avec des valeurs d'entrées de métabolites principaux choisies. Entrée d'oxygene,Glucose et acide gras requis.
Le modèle est considéré comme basé sur MitoCore. si ce n'est pas le cas, alors il faut modifier les id des réactions associées.
Les métabolites principaux sont : glucose, acide gras, oxygène, acétoacétate, hydroxybutyrate,lactate,bicarbonate.
#### plot_voie_metabolique_ou_accoa()
fonction qui représente les résultats produits par la fonction define_boundary_and_run_model.
il faut lui donner un dictionnaire de dictionnaire résultats.
#### run_model_calpainopathy()
fonction qui récupère les valeurs de flux d'un modèle sain puis modifie les Upperbounds des réactions comme infiqué dans le fichier model.convertion.csv 
WARNING : Il faut avoir fait tourner le modèle sain d'abord (model.optimize())
#### heatmap_flux()
Fonction qui plot un heatmap des flux en utilisant Seaborn.
la fonction prend n'importe quel nombre d'objet solution produit par run_model_calpainopathie() ou define_boundary_and_run_model().
