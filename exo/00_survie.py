"""Script de survie — mobilise les 5 concepts du kit."""
from pathlib import Path

# Concept 1 : variables et types
nom = "Alice"
notes = [12, 15, 18, 9, 20]

# Concept 3 : fonction qui calcule une moyenne
def moyenne(valeurs):
    return sum(valeurs) / len(valeurs)

# Concept 2 + 3 : condition pour déterminer la mention
def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    else:
        return "Passable"

# Concept 4 : dictionnaire de résultats
resultat = {
    "nom": nom,
    "notes": notes,
    "moyenne": moyenne(notes),
    "mention": mention(moyenne(notes)),
}

# Concept 5 : import (Path) + boucle (concept 2)
print(f"Résultat pour {resultat['nom']} :")
for cle, valeur in resultat.items():
    print(f"  - {cle} : {valeur}")