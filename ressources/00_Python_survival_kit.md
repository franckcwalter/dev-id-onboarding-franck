# Python — Kit de survie

> Durée de lecture + pratique : 60-90 min
> Pré-requis : Python 3.11+ installé, un éditeur ouvert (VS Code, PyCharm, ou
> un simple éditeur texte), savoir lancer une commande dans un terminal.
> **À faire si** : tu as raté 2+ questions du bloc 1 du test de positionnement,
> OU tu n'as pas écrit de Python depuis longtemps, OU tu débutes en Python.

## Pourquoi cette techno ?

Ce mini-cours **n'est pas un cours de Python complet**. C'est le strict minimum
pour être autonome dans le reste du brief P0 et le mini-cours
[`05_Python_essentiel.md`](./05_Python_essentiel.md).

L'objectif unique : **lire et modifier du code Python sans paniquer**.

Si tu sais déjà écrire une fonction, faire une boucle `for`, manipuler une
liste et un dictionnaire, lancer un script et lire un message d'erreur → tu
peux **passer directement** au mini-cours suivant. Ce kit est conçu pour ceux
qui ne sont pas dans cette situation, ou qui veulent dérouiller.

**Tout ce qui n'est PAS dans ce kit** (classes, héritage, async, generators,
décorateurs, lambdas, comprehensions, type hints, packaging, virtualenv,
pandas) sera traité ailleurs **quand** ce sera utile. Pas avant.

> 💡 **Comment travailler ce module**
>
> Ne cherche pas à mémoriser toute la syntaxe. L'objectif est :
> - **reconnaître** les structures quand tu les croises ;
> - **modifier** un exemple existant pour qu'il fasse ce que tu veux ;
> - **comprendre** les messages d'erreur les plus fréquents.
>
> Copier-coller un exemple puis le modifier est **la** façon normale
> d'apprendre Python au début. Pas de honte à ça.

## Concepts clés

### 1. Variables et types de base

Une variable, c'est un nom qui pointe vers une valeur. Pas besoin de déclarer
le type : en Python, **le type est porté par la valeur, pas par la variable**.

```python
nom = "Alice"          # str (chaîne de caractères)
age = 30               # int (entier)
prix = 12.5            # float (nombre à virgule)
actif = True           # bool (True ou False)
```

**À retenir** :
- Une chaîne s'écrit entre `"..."` ou `'...'`, peu importe lequel.
- `30` (sans guillemets) est un nombre, `"30"` (avec) est une chaîne. Ce n'est
  pas la même chose : `30 + 1` vaut `31`, `"30" + 1` produit une erreur.
- `True` et `False` prennent une majuscule (pas `true`).

**Vérifier le type d'une valeur** :

```python
type(age)        # <class 'int'>
type(nom)        # <class 'str'>
```

> 💡 `type(...)` est surtout un outil de **debug / inspection** quand tu veux
> comprendre une erreur ou vérifier ce qu'une fonction t'a renvoyé. Tu n'as
> pas besoin de l'appeler partout dans ton code applicatif.

### 2. Conditions et boucles

Une condition exécute du code **si** quelque chose est vrai. Une boucle répète
du code pour chaque élément.

```python
# Condition (if / elif / else)
prix = 15
if prix > 10:
    print("Trop cher")
elif prix > 5:
    print("Raisonnable")
else:
    print("Pas cher")
```

```python
# Boucle for (parcourir une séquence)
notes = [12, 15, 18, 9]
for note in notes:
    print(note)
```

**À retenir** :
- L'**indentation** délimite les blocs en Python (pas de `{...}` comme en
  Java/JS). La convention universelle est **4 espaces** (PEP 8, Black, Ruff,
  VS Code, PyCharm — tout le monde s'aligne là-dessus). **Ne mélange jamais
  tabs et espaces** : c'est la première source de bug d'un débutant Python.
- Les **deux-points `:`** sont obligatoires à la fin de `if`, `elif`, `else`,
  `for`, `while`.
- `for x in liste:` itère **directement** sur les éléments, pas sur les indices.

### 3. Fonctions

Une fonction, c'est un bout de code nommé qu'on peut **réutiliser**.

```python
def addition(a, b):
    return a + b

# Appel
resultat = addition(3, 5)    # resultat vaut 8
```

**Anatomie** :
- `def` : mot-clé qui démarre une définition de fonction.
- `addition` : nom de la fonction.
- `(a, b)` : **paramètres** (ce que la fonction reçoit).
- `return a + b` : **valeur de retour** (ce que la fonction renvoie).
- `addition(3, 5)` : **appel** (3 et 5 sont des **arguments**).

**Pièges fréquents** :

```python
def afficher(message):
    print(message)
    # pas de return → la fonction renvoie None par défaut

valeur = afficher("salut")   # valeur vaut None, pas "salut" !
```

**Portée des variables** : une variable créée dans une fonction n'existe pas
en dehors.

```python
def calculer():
    x = 10
    return x

print(x)   # ❌ NameError : x n'existe pas ici
```

### 4. Listes et dictionnaires

Ce sont les **2 structures de données** qu'on utilise partout (configs,
payloads API, réponses JSON, datasets).

**Liste** — séquence ordonnée d'éléments :

```python
notes = [12, 15, 18, 9]

notes[0]            # 12 (premier élément, on compte à partir de 0)
notes[-1]           # 9 (dernier élément)
len(notes)          # 4 (nombre d'éléments)
notes.append(20)    # ajoute 20 à la fin (modifie la liste sur place)
print(notes)        # [12, 15, 18, 9, 20]
```

> ⚠️ **Piège classique** : `notes.append(20)` **modifie la liste sur place** et
> renvoie `None`. Donc **n'écris jamais** :
> ```python
> notes = notes.append(20)   # ❌ notes vaut désormais None
> ```
> Écris simplement `notes.append(20)` sur une ligne, sans réassignation.

**Dictionnaire** — association clé → valeur :

```python
user = {
    "nom": "Alice",
    "age": 30,
    "actif": True,
}

user["nom"]              # "Alice"
user["age"] = 31         # modifie la valeur
user["email"] = "a@x.fr" # ajoute une nouvelle clé
"nom" in user            # True (test d'appartenance)
```

**À retenir** :
- Listes : `[...]` avec crochets, indexées par **position** (0, 1, 2…).
- Dicts : `{...}` avec accolades, indexés par **clé** (string en général).
- Un payload JSON d'API qui arrive en Python devient un dict.

### 5. Imports et lire une traceback

**Imports** — utiliser du code venant d'ailleurs (stdlib ou libs installées).

```python
import json                      # import du module entier
from pathlib import Path         # import d'un objet précis
import pandas as pd              # import avec alias

# Utilisation
data = json.loads('{"a": 1}')
chemin = Path("data/input.csv")    # crée un objet représentant un chemin
df = pd.DataFrame({"x": [1, 2]})
```

**À retenir** :
- Les imports vont **au début du fichier**.
- `import json` → on utilise `json.loads(...)`.
- `from pathlib import Path` → on utilise `Path(...)` directement.
- `Path(...)` n'ouvre pas le fichier : il crée juste un **objet** qui
  représente le chemin, qu'on pourra ensuite passer à des fonctions de
  lecture/écriture.

**Lire une traceback** — quand Python plante, il affiche une erreur. Apprends à
la lire **du bas vers le haut**.

Exemple :

```
Traceback (most recent call last):
  File "script.py", line 7, in <module>
    resultat = addition("trois", 5)
  File "script.py", line 2, in addition
    return a + b
TypeError: unsupported operand type(s) for +: 'str' and 'int'
```

**Comment décoder** :
1. **Dernière ligne** = type d'erreur + message → `TypeError: ...`.
2. **Ligne juste au-dessus** = l'instruction qui a planté → `return a + b`.
3. **Ligne du dessus** = qui a appelé cette fonction → `addition("trois", 5)`.
4. **Diagnostic** : on a passé `"trois"` (str) au lieu d'un nombre.

**Les 4 erreurs les plus fréquentes** :

| Erreur | Ce que ça veut dire |
|---|---|
| `NameError: name 'x' is not defined` | Variable utilisée mais jamais créée (typo ? oubli d'import ?) |
| `TypeError: ...` | Mauvais type passé à une opération (`"3" + 5`, ou `len(42)`) |
| `IndexError: list index out of range` | Tu accèdes à un élément qui n'existe pas (`liste[10]` sur une liste de 5) |
| `KeyError: 'truc'` | Clé inexistante dans un dict (`user["telephone"]` qui n'a jamais été défini) |

## Exemple minimal qui tourne

Sauvegarde ce script sous `survie.py`, lance `python survie.py`.

```python
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
```

**Sortie attendue** :
```
Résultat pour Alice :
  - nom : Alice
  - notes : [12, 15, 18, 9, 20]
  - moyenne : 14.8
  - mention : Bien
```

## Exercice guidé — 10 micro-questions

À faire dans un fichier `exo_survie.py`. Chaque question prend 1-3 minutes.
Lance `python exo_survie.py` après chaque modification pour vérifier.

1. **Variable** — crée une variable `age` qui contient ton âge, puis affiche
   `"J'ai 25 ans"` (ou ton âge) avec une f-string.
2. **Type** — affiche le **type** de `age`, puis crée `age_str = "25"` et
   affiche son type. Constate la différence.
3. **Condition** — écris un `if` qui affiche `"majeur"` si `age >= 18`, sinon
   `"mineur"`.
4. **Boucle** — crée une liste `[1, 2, 3, 4, 5]` et affiche **le carré** de
   chaque nombre (boucle `for`, opérateur `**`).
5. **Fonction** — écris une fonction `est_pair(n)` qui renvoie `True` si `n`
   est pair, `False` sinon. Teste-la avec `est_pair(4)` et `est_pair(7)`.
6. **Liste** — crée une liste `villes = ["Paris", "Lyon", "Marseille"]`,
   ajoute `"Toulouse"` à la fin, puis affiche le **dernier élément**.
7. **Dictionnaire** — crée un dict `personne` avec les clés `nom`, `age`,
   `ville`. Affiche le nom, puis modifie l'âge.
8. **Boucle sur un dict** — affiche **toutes les clés et valeurs** du dict
   `personne` (indice : `.items()`).
9. **Import** — importe `Path` depuis `pathlib`, crée `chemin = Path("data") /
   "file.txt"`, affiche `chemin`.
10. **Traceback** — écris volontairement `print(toto)` (sans avoir défini
    `toto`), lance le script, **lis la traceback du bas vers le haut**,
    identifie le type d'erreur et la ligne fautive.

<details>
<summary>Voir la solution</summary>

```python
from pathlib import Path

# 1.
age = 25
print(f"J'ai {age} ans")

# 2.
print(type(age))           # <class 'int'>
age_str = "25"
print(type(age_str))       # <class 'str'>

# 3.
if age >= 18:
    print("majeur")
else:
    print("mineur")

# 4.
for n in [1, 2, 3, 4, 5]:
    print(n ** 2)

# 5.
def est_pair(n):
    return n % 2 == 0
print(est_pair(4))          # True
print(est_pair(7))          # False

# 6.
villes = ["Paris", "Lyon", "Marseille"]
villes.append("Toulouse")
print(villes[-1])           # "Toulouse"

# 7.
personne = {"nom": "Alice", "age": 30, "ville": "Paris"}
print(personne["nom"])      # "Alice"
personne["age"] = 31

# 8.
for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")

# 9.
chemin = Path("data") / "file.txt"
print(chemin)               # data/file.txt (ou data\file.txt sur Windows)

# 10.
# print(toto) → NameError: name 'toto' is not defined
# Diagnostic : variable jamais créée, vérifier l'orthographe ou un oubli de définition.
```

</details>

## Pièges fréquents

| Piège | Conséquence |
|---|---|
| Indentation incohérente (mélange tabs/espaces) | `IndentationError` ou `TabError` — Python ne peut pas parser |
| Oublier les deux-points après `if`, `for`, `def` | `SyntaxError: expected ':'` |
| Confondre `=` (assignation) et `==` (test d'égalité) | `if x = 5:` plante, `if x == 5:` marche |
| Indexer à partir de 1 au lieu de 0 | `liste[1]` renvoie le **2e** élément, pas le premier |
| Modifier un dict pendant qu'on itère dessus | `RuntimeError: dictionary changed size during iteration` |
| Oublier `return` dans une fonction | La fonction renvoie `None` silencieusement |

**Symptôme → cause probable** :

| Symptôme | Cause probable |
|---|---|
| `NameError: name 'X' is not defined` | Variable jamais créée, ou faute de frappe, ou oubli d'import |
| `TypeError: unsupported operand type(s)` | Mélange de types (`"3" + 5`, ou opération entre str et int) |
| `IndexError: list index out of range` | Index trop grand pour la taille de la liste |
| `KeyError: 'X'` | Clé absente du dict — utiliser `.get("X")` qui renvoie `None` à la place |
| `IndentationError` | Tabs/espaces mélangés, ou bloc mal indenté |

## Pour aller plus loin

**Si tu as fini ce kit en 60 min et que ça t'a paru facile** :
→ passe au mini-cours [`05_Python_essentiel.md`](./05_Python_essentiel.md).

**Si tu veux consolider avant d'aller plus loin** :
- **Tutoriel Python officiel (FR)** — chapitres 3 à 5 :
  <https://docs.python.org/fr/3/tutorial/introduction.html>
- **Real Python — Python Basics** (en anglais, gratuit) :
  <https://realpython.com/python-first-steps/>

## Vérification (checklist apprenant)

- [ ] J'ai lancé `survie.py` et obtenu la sortie attendue.
- [ ] J'ai fait les 10 micro-exercices, et je comprends chaque solution.
- [ ] Je sais expliquer la différence entre `30` et `"30"`.
- [ ] Je sais écrire une fonction avec paramètres et `return`.
- [ ] Je sais différencier une liste (`[...]`) d'un dictionnaire (`{...}`).
- [ ] Je sais lire une traceback du bas vers le haut et identifier la ligne
      fautive.
- [ ] Je connais les 4 erreurs courantes (`NameError`, `TypeError`,
      `IndexError`, `KeyError`).
- [ ] Je peux passer au mini-cours `05_Python_essentiel.md` sans appréhension.
