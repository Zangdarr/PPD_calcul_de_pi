# PPD_calcul_de_pi
Calcul de pi en parallèle avec Grid5000

La formule qui va être parallélisé est la suivante :

π = 4 arctan1 = 4 * ( somme pour k=0 à ∞ de (((−1)^k) / (2k + 1)))

part_of_pi.py sert à calculer la somme de la formule. Le découpage en part égale du travail entre les unité de calcul est fait à l'aide un "pas". Par exemple, si l'on a 4 unités, la première unité va calculé pour k = 0, 4, 8, 12, etc. La seconde va calculer pour k = 1, 5, 9, 13, etc.
