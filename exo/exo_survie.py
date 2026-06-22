

# 1
age = 31
print(f"J'ai {age} ans")

# 2
print(type(age))
age_str = "25"
print(type(age_str))

# 3
if age>=18:
    print("majeur")
else:
    print("mineur")

# 4
nb_list = [1,2,3,4,5]
for nb in nb_list:
    print(nb**2)

# 5
def est_pair(n):
    return n%2 == 0

print(est_pair(4))
print(est_pair(7))

# 6
villes = ["Paris", "Lyon", "Marseille"]
villes.append("Toulouse")

print(villes[-1])

# 7
personne = {
    "nom": "Franck",
    "age": 31,
    "ville": "Strasbourg"
}

print(personne["nom"])
personne["age"] = 32
print(personne["age"])
# 8
for key, value in personne.items():
    print(f"key:{key}, value: {value}")

# 9
## devrait être en haut du fichier
from pathlib import Path
chemin = Path("data") / "file.txt"
print(chemin)

# 10
print(toto)
# NameError .54