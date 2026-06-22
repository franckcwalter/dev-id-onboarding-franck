# Versions testées : python 3.11, numpy 2.x

# importe numpy et lui donne l'alias "np" (convention universelle)
import numpy as np

# Création

# crée un tableau numpy (ndarray) à partir d'une liste Python
a = np.array([1, 2, 3, 4, 5])
# comme range() : de 0 (inclus) à 10 (exclu) par pas de 2 -> [0, 2, 4, 6, 8]
b = np.arange(0, 10, 2)
# matrice 3 lignes x 4 colonnes remplie de 0.0 (le tuple (3,4) = la "shape")
m = np.zeros((3, 4))
# default_rng(42) = générateur aléatoire avec graine 42 (résultats reproductibles)
# .normal(...) = tire des nombres dans une loi normale : moyenne (loc)=0, écart-type (scale)=1, forme 3x4
r = np.random.default_rng(42).normal(loc=0, scale=1, size=(3, 4))

# Inspection

# .shape = dimensions du tableau -> (5,) : 1 dimension de 5 éléments
print("a.shape  =", a.shape)
# .dtype = type des éléments stockés -> int64 (entiers)
print("a.dtype  =", a.dtype)
# .mean() = moyenne de tous les éléments ; .round(3) = arrondi à 3 décimales
print("r.mean() =", r.mean().round(3))

# Vectorisation

# l'opération s'applique à CHAQUE élément d'un coup, sans boucle -> [10 20 30 40 50]
print("a * 10   =", a * 10)
# b[:5] = les 5 premiers éléments de b ; addition élément par élément -> [1 4 7 10 13]
print("a + b[:5]=", a + b[:5])

# Indexation booléenne

# a % 2 == 0 crée un masque [F,T,F,T,F] ; a[masque] garde les éléments True -> [2 4]
print("pairs    =", a[a % 2 == 0])

# Broadcasting

# le scalaire 100 est "diffusé" sur toute la matrice (ajouté à chaque case), puis arrondi à 2 décimales
print("r + 100  =\n", (r + 100).round(2))
