# Python essentiel — Mini-cours

> Durée de lecture + pratique : ~45 min
> Pré-requis : Python 3.11+ installé, environnement virtuel actif, savoir lancer un script `python script.py`.

## Pourquoi cette techno ?

Vous savez tous lire du Python. Ce mini-cours ne reprend pas les fondamentaux
(variables, boucles, fonctions). Il cible **5 idiomes Python que FastAPI,
Pydantic, pytest, scikit-learn et Docker supposent acquis**, et que les profils
IT/dev maîtrisent à des degrés variables.

L'enjeu n'est pas de réécrire Python. C'est de **passer de « je sais lire du
Python » à « j'écris du Python sur lequel les libs du parcours s'appuient sans
friction »**.

> 🌱 **Ce mini-cours suppose que vous savez déjà** :
> - écrire une fonction (`def`) avec paramètres et `return` ;
> - utiliser `if`, `for`, listes et dictionnaires ;
> - lancer un script Python (`python script.py`) ;
> - lire une erreur simple (`NameError`, `TypeError`, `IndexError`, `KeyError`).
>
> Si ce n'est pas le cas, **commence par** le pré-module
> [`00_Python_survival_kit.md`](./00_Python_survival_kit.md) (60-90 min). Tu
> reviendras ici ensuite, prêt·e à absorber les idiomes modernes.

> 💡 **Comment lire ce mini-cours**
>
> Ne cherchez pas à mémoriser toute la syntaxe. L'objectif est de **reconnaître
> les idiomes** qui reviennent partout dans FastAPI, pytest et les projets
> Python modernes.
>
> Concentrez-vous sur :
> - **reconnaître** les patterns quand vous les croiserez ;
> - **savoir les relire** sans buter ;
> - **savoir les modifier** quand vous touchez à du code existant ;
> - **comprendre pourquoi** ils existent (ce que la convention vous évite).
>
> La syntaxe précise se mémorise avec la pratique. Les conventions mentales,
> elles, doivent être installées dès maintenant.

| Lib utilisée dans le parcours | Idiome Python sur lequel elle repose |
|---|---|
| FastAPI (M0-B1, M1-B2, M5) | type hints, décorateurs |
| Pydantic v2 (M1-B2 → M9) | type hints |
| pytest (M0 → M9) | décorateurs, fixtures, context managers |
| `joblib.dump` / `open` (M0-B1+) | context managers |
| scikit-learn / FastAPI errors (M1+) | exceptions spécifiques |
| Tout I/O fichier / modèle (M0 → M9) | `pathlib.Path` |

**Alternatives à connaître** : les fondamentaux Python n'ont pas d'alternative
sur ce parcours. Ils sont mobilisés partout.

## Concepts clés

### 1. Type hints — déclarer les contrats des fonctions

Les **type hints** (PEP 484, 526, 604) déclarent les types attendus en entrée
et en sortie d'une fonction. Ils ne **bloquent pas** l'exécution (Python reste
dynamique), mais ils sont **lus par FastAPI, Pydantic, votre IDE et `mypy`**
pour générer doc, validations et auto-complétion.

> ⚠️ **Précision importante** : les type hints n'effectuent **aucune validation
> runtime native**. `def f(x: int)` appelé avec `f("trois")` ne plantera pas
> sur la signature — Python continue. La validation runtime, c'est **Pydantic**
> (ou un `isinstance` explicite). Les hints sont une **promesse au lecteur et
> aux outils**, pas un garde-fou d'exécution.

**Signature lisible vs signature opaque** :

```python
# ❌ Opaque — on ne sait pas ce que la fonction attend ni ce qu'elle rend
def predict(x, y):
    return 4500 * x + 12000 * y

# ✅ Lisible — la signature documente le contrat
def predict(surface_m2: float, nb_pieces: int) -> float:
    return 4500 * surface_m2 + 12000 * nb_pieces
```

Les bénéfices d'une signature typée vont bien au-delà de `mypy` :
- **auto-documentation** : votre code est sa propre doc, plus besoin de
  paragraphes explicatifs sur « ce que doit être `x` ».
- **IDE** : auto-complétion correcte (`.lower()` proposé sur un `str`, pas sur
  un `int`).
- **maintenance** : 6 mois plus tard, vous savez quel type un appelant doit
  fournir sans relire l'implémentation.
- **onboarding** : un nouvel arrivant lit la signature, pas le corps.

**Syntaxe Python 3.10+** à préférer (vous n'avez pas besoin des imports
`typing.List`, `typing.Optional`, etc. qu'on voit dans le legacy) :

```python
# Préférer (3.10+)              Plutôt que (legacy)
liste_prix: list[float]         List[float]
mapping: dict[str, int]         Dict[str, int]
optionnel: str | None           Optional[str]
union: int | float              Union[int, float]
```

**Pourquoi c'est central sur ce parcours** : FastAPI lit la signature d'une
fonction de route et en déduit (a) comment valider le payload, (b) la doc
Swagger, (c) la sérialisation JSON. Sans type hints, tout est cassé.

```python
@app.post("/predict")
def predict(surface_m2: float, nb_pieces: int) -> dict[str, float]:
    # FastAPI valide automatiquement que surface_m2 est un float
    return {"prix": predire_prix(surface_m2, nb_pieces)}
```

Préférez **`dict[str, float]`** à `dict` tout court : le contrat est plus
précis, et l'IDE de l'appelant saura que `response["prix"]` est un `float`.
Pour des structures plus complexes (clés fixes, types hétérogènes), on
montera en M1-B2 vers un modèle Pydantic — bien plus expressif qu'un
`TypedDict`.

### 2. Décorateurs — modifier le comportement d'une fonction

Un décorateur est **une fonction qui prend une fonction et renvoie une fonction
modifiée**. Le `@` est juste du sucre syntaxique :

```python
@pytest.fixture
def client():
    return TestClient(app)

# strictement équivalent à :
def client():
    return TestClient(app)
client = pytest.fixture(client)
```

**Les 3 décorateurs incontournables du parcours** :

```python
# 1. Routes FastAPI
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

# 2. Fixtures pytest
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

# 3. Paramétrisation de tests
@pytest.mark.parametrize("surface, prix_min", [(30, 100_000), (65, 200_000)])
def test_predict(client, surface, prix_min):
    response = client.post("/predict", json={"surface_m2": surface})
    assert response.json()["prix"] >= prix_min
```

**À retenir** : un décorateur n'a rien de magique. C'est une fonction qui en
prend une autre. Vous pouvez tout à fait l'écrire à la main si besoin.

### 3. Context managers (`with`) — gérer proprement les ressources

Un context manager garantit qu'une ressource (fichier, connexion, lock, app
FastAPI) est **correctement libérée**, même en cas d'exception.

```python
# ❌ Risque : si une exception survient entre open() et close(),
#    le fichier reste ouvert et bloque le système.
f = open("transactions.csv", encoding="utf-8")
data = f.read()
f.close()

# ✅ Le `with` garantit la fermeture quoi qu'il arrive.
with open("transactions.csv", encoding="utf-8") as f:
    data = f.read()
```

> ⚠️ **Toujours préciser `encoding="utf-8"`** quand vous ouvrez un fichier
> texte. L'encodage par défaut dépend de l'OS (Windows lit en cp1252, Linux/Mac
> en UTF-8). Sans ce paramètre, vos tests passent en local et plantent en CI ou
> chez un collègue Windows dès qu'un accent apparaît.

**Usages omniprésents dans le parcours** :

```python
# Lecture de fichier (M0-B1, P0)
with open("config.yaml", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# TestClient FastAPI (M0-B1+) — déclenche le lifespan (chargement du modèle)
with TestClient(app) as client:
    response = client.get("/health")

# Écriture binaire (sérialisation modèle joblib) — pas d'encoding pour le binaire
with open("model.joblib", "wb") as f:
    joblib.dump(model, f, compress=3)
```

> 💡 En pratique on écrit souvent `joblib.dump(model, "model.joblib", compress=3)`
> directement — joblib gère l'ouverture/fermeture en interne. La forme avec
> `with open(..., "wb")` ci-dessus n'est qu'un exemple pédagogique pour
> illustrer le context manager.

**À retenir** : si une lib documente un usage avec `with`, **utilisez `with`**.
Sinon vous risquez fuites de mémoire et fichiers verrouillés.

### 4. Gestion d'exceptions — EAFP plutôt que LBYL

Python encourage le style **EAFP** (*Easier to Ask Forgiveness than Permission*) :
on tente l'opération et on rattrape l'exception, plutôt que de vérifier
préventivement chaque condition (style **LBYL** = *Look Before You Leap*).

```python
# Style LBYL (défensif) — fragile, on oublie toujours un cas
def division_safe(a, b):
    if not isinstance(a, (int, float)):
        return "Type invalide"
    if not isinstance(b, (int, float)):
        return "Type invalide"
    if b == 0:
        return "Division impossible"
    return a / b
    # Et les booléens ? Et les Decimal ? Et b ≈ 0 par flottement ?

# Style EAFP (pythonique) — couvre les cas qu'on n'a pas anticipés
def division_safe(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division impossible"
    except TypeError:
        return "Type invalide"
```

**Règles d'or** :
1. **Toujours catcher une exception spécifique**, jamais `except:` ou
   `except Exception:` tout court — sauf aux frontières (cf. nuance ci-dessous).
2. **Ordonner les `except` du plus spécifique au plus général** — le premier
   qui matche gagne.
3. **Validation de données externes** (payload API) : laissez **Pydantic** le
   faire en LBYL automatisé. C'est son métier.
4. **Logique métier interne** : EAFP.

**Anti-pattern à éviter** :

```python
# ❌ Bare except masque tous les bugs (NameError, KeyboardInterrupt, etc.)
try:
    result = process(data)
except:
    result = None

# ✅ Catcher ce qu'on attend, laisser remonter le reste
try:
    result = process(data)
except (ValueError, KeyError) as e:
    logger.warning(f"Échec process : {e}")
    result = None
```

**Nuance importante — les frontières applicatives** :

L'interdiction « jamais `except Exception:` » est globalement saine, mais elle
admet **une exception légitime** : aux **frontières d'une application**, on
veut souvent attraper *tout ce qui peut arriver*, **logger**, puis soit
**rollback**, soit **re-raise**. Sinon une exception non prévue fait tomber
l'application entière.

Cas typiques :
- **Boucle worker** (consumer Kafka, scheduler) — une exception sur un message
  ne doit pas tuer le worker entier
- **Endpoint API au plus haut niveau** — middleware d'erreur qui logge et
  renvoie un 500 propre
- **CLI** — affichage propre + code de sortie ≠ stack trace brute à l'utilisateur

```python
# ✅ Acceptable aux frontières — avec logging et re-raise éventuel
def boucle_worker(messages):
    for msg in messages:
        try:
            traiter(msg)
        except Exception as e:
            logger.exception(f"Échec traitement message {msg.id} : {e}")
            metrics.increment("worker.errors")
            # selon le contexte : continue (next message) ou raise (kill worker)
```

**Règle pratique** : `except Exception:` est acceptable **uniquement** aux
frontières applicatives, **toujours** assorti d'un logging avec contexte et
d'une décision explicite (continue / re-raise / fallback). Dans tout le reste
du code (logique métier, helpers), exception spécifique obligatoire.

### 5. `pathlib.Path` — manipuler les chemins

`pathlib.Path` est la **manière moderne** de manipuler des chemins de fichiers.
Elle remplace `os.path` (qui reste dans le legacy mais est plus verbeux et
moins sûr cross-plateforme).

```python
from pathlib import Path

# Construction de chemins (sans concaténation de strings)
data_dir = Path("data")
csv_file = data_dir / "transactions.csv"
print(csv_file)  # data/transactions.csv (slash automatique selon OS)

# Existence, type
csv_file.exists()       # True/False
csv_file.is_file()      # True/False
data_dir.is_dir()       # True/False

# Lecture/écriture rapide — équivalents compacts qui gèrent le `with` en interne
contenu = csv_file.read_text(encoding="utf-8")
csv_file.write_text("nouveau contenu", encoding="utf-8")
# (équivalent à : `with csv_file.open(...) as f: contenu = f.read()`)

# Parties du chemin
csv_file.name            # 'transactions.csv'
csv_file.stem            # 'transactions'
csv_file.suffix          # '.csv'
csv_file.parent          # Path('data')

# Création de dossier
Path("data/processed").mkdir(parents=True, exist_ok=True)

# Lister un dossier
for p in Path("data").glob("*.csv"):
    print(p)
```

**Le piège cross-platform qui mord tout le monde une fois** :

```python
# ❌ Casse sur Linux/Mac (cherche un fichier littéralement nommé "path\to\file")
chemin = "data\\input.txt"

# ❌ Casse sur Windows (le séparateur n'est pas /)
chemin = "data/" + filename

# ⚠️ Fonctionne, mais legacy : plus verbeux, moins lisible, moins ergonomique
chemin = os.path.join("data", filename)

# ✅ Cross-platform garanti, lisible, composable avec /
chemin = Path("data") / filename
```

Vos tests passent en local sur Mac/Linux, votre CI tourne sur un runner
Windows (ou l'inverse) → boom. **`Path` règle ce problème une fois pour
toutes**, plus le séparateur n'est jamais une question.

**À retenir** : `Path` partout, jamais de concaténation `"data" + "/" +
"transactions.csv"` ou `os.path.join`.

## Exemple minimal qui tourne

Un script qui mobilise les 5 concepts. Sauvegardez sous `demo_python.py` et
lancez `python demo_python.py`.

```python
"""Démo des 5 idiomes Python essentiels du parcours."""
from pathlib import Path
from functools import wraps
import json

# === 1. Type hints ===
def predire_prix(surface_m2: float, nb_pieces: int) -> float:
    """Estime le prix d'un appartement (formule jouet)."""
    return 4500 * surface_m2 + 12000 * nb_pieces


# === 2. Décorateurs (on écrit le nôtre pour montrer que ce n'est pas magique) ===
def log_call(func):
    """Décorateur qui logge chaque appel d'une fonction."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"→ appel {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"← retour {result!r}")
        return result
    return wrapper

@log_call
def predire_loge(surface_m2: float, nb_pieces: int) -> float:
    return predire_prix(surface_m2, nb_pieces)


# === 3. Context manager + pathlib ===
data_dir = Path("data_demo")
data_dir.mkdir(exist_ok=True)
config_file = data_dir / "config.json"

config = {"taux_tva": 0.20, "marge_securite": 0.05}
with config_file.open("w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)


# === 4. Gestion d'exceptions (EAFP, exception spécifique) ===
def charger_config(chemin: Path) -> dict[str, float]:
    try:
        with chemin.open(encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  Config absente, défauts utilisés.")
        return {"taux_tva": 0.20, "marge_securite": 0.10}
    except json.JSONDecodeError as e:
        print(f"⚠️  Config corrompue : {e}, défauts utilisés.")
        return {"taux_tva": 0.20, "marge_securite": 0.10}


# === Mise en pratique ===
if __name__ == "__main__":
    cfg = charger_config(config_file)
    prix_ht = predire_loge(surface_m2=65, nb_pieces=3)
    prix_ttc = prix_ht * (1 + cfg["taux_tva"])
    print(f"\nPrix HT : {prix_ht:,.0f} €")
    print(f"Prix TTC : {prix_ttc:,.0f} €")
```

**Sortie attendue** :
```
→ appel predire_loge((), {'surface_m2': 65, 'nb_pieces': 3})
← retour 328500.0

Prix HT : 328,500 €
Prix TTC : 394,200 €
```

## Exercice guidé

Refactorez le script ci-dessous (style « junior pressé ») en code idiomatique
mobilisant les 5 concepts.

**Code de départ** (`exo_python_start.py`) :

```python
import os

def predire(surf, nb):
    try:
        return 4500 * float(surf) + 12000 * int(nb)
    except:
        return -1

def charger(p):
    if os.path.exists(p):
        f = open(p)
        contenu = f.read()
        f.close()
        return contenu
    else:
        return ""

if __name__ == "__main__":
    path = "data" + "/" + "input.txt"
    data = charger(path)
    prix = predire("65", "3")
    print("prix = " + str(prix))
```

**Consignes** :
1. Ajouter des type hints sur les deux fonctions.
2. Remplacer le `try/except:` bare par une exception spécifique.
3. Utiliser `pathlib.Path` au lieu de `os.path` et de la concaténation.
4. Utiliser un `with` pour ouvrir le fichier.
5. Remplacer `"prix = " + str(prix)` par une f-string.
6. **Bonus** : écrire un décorateur `@log_call` qui logge les appels de
   `predire`.

**Solution attendue** (à consulter après avoir essayé) :

<details>
<summary>Voir la solution</summary>

```python
from pathlib import Path
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"→ {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"← {result!r}")
        return result
    return wrapper

@log_call
def predire(surface_m2: float, nb_pieces: int) -> float:
    return 4500 * surface_m2 + 12000 * nb_pieces

def charger(chemin: Path) -> str:
    try:
        with chemin.open(encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

if __name__ == "__main__":
    path = Path("data") / "input.txt"
    data = charger(path)
    prix = predire(surface_m2=65, nb_pieces=3)
    print(f"prix = {prix:,.0f} €")
```

**Points de vérification** :
- Type hints partout, avec types modernes (`float`, `int`, `str`, `Path`).
- Exception spécifique `FileNotFoundError` au lieu du bare except.
- `Path("data") / "input.txt"` au lieu de la concaténation.
- `with chemin.open(...)` au lieu du `open()` / `close()` manuel.
- f-string `f"prix = {prix:,.0f} €"` au lieu de la concaténation.
- Le décorateur `@log_call` est appelé une seule fois à la définition de
  `predire`, et le wrapper s'exécute à chaque appel.

</details>

## Pièges fréquents

| Piège | Conséquence |
|---|---|
| `except:` ou `except Exception:` sans précision | Masque des bugs (NameError, TypeError, KeyboardInterrupt) — débogage cauchemardesque |
| Argument par défaut mutable (`def f(x=[])`) | La liste est partagée entre tous les appels — bug subtil et difficile à reproduire |
| `os.path.join` ou concaténation de strings pour les chemins | Casse sur Windows / Linux selon le séparateur, et illisible |
| Ouvrir un fichier sans `with` | Fichier qui reste ouvert si exception → fuite handle / lock système |
| Oublier `from __future__` ou `typing.List` en Python 3.8 | Type hints qui plantent — utilisez Python 3.11+ pour `list[int]` natif |
| `print()` dans du code applicatif long terme ou en prod | Pas de niveau, pas de timestamp, pas de filtrage prod/dev — à partir de M1, préférez `logging` ou `loguru`. `print()` reste OK pour scripts ad hoc, notebooks et debug local. |

**Symptôme → cause probable** :

| Symptôme | Cause probable |
|---|---|
| `TypeError: 'int' object is not subscriptable` | Vous indexez un int comme si c'était une liste — type hints auraient flaggé ça |
| Tests pytest qui passent en local mais plantent en CI sur Windows | Chemins en dur avec `/` au lieu de `Path` — séparateur de chemin |
| Comportement bizarre, une liste qui « grandit toute seule » entre appels | Argument par défaut mutable — voir ci-dessus |
| `ResourceWarning: unclosed file` | `open()` sans `with`, ou exception entre `open` et `close` |
| Test pytest qui dit `'FixtureFunctionDefinition' has no attribute 'X'` | Fixture demandée mais paramètre absent de la signature du test |

## Pour aller plus loin

**Documentation officielle** :
- Tutoriel Python officiel (FR) : <https://docs.python.org/fr/3/tutorial/>
- `pathlib` : <https://docs.python.org/fr/3/library/pathlib.html>
- Type hints (PEP 484) : <https://peps.python.org/pep-0484/>
- Décorateurs : <https://docs.python.org/fr/3/glossary.html#term-decorator>

**Ressources approfondies** :
- *Real Python* — articles courts et concrets, en particulier sur les
  décorateurs : <https://realpython.com/primer-on-python-decorators/>

**Standards de code** :
- `ruff` (linter + formatter ultra-rapide, remplace flake8 + isort + black) :
  <https://docs.astral.sh/ruff/>
- `mypy` (type checker) : <https://mypy.readthedocs.io/>

**À ne pas survoler** (utile dès M0-B1) :
- Le tableau « Symptôme → cause probable » ci-dessus : à relire après votre
  premier test pytest cassé, ça vous fera gagner du temps.

## Vérification (checklist apprenant)

- [ ] J'ai lancé `demo_python.py` sans erreur, et la sortie correspond.
- [ ] J'ai refait l'exercice guidé en moins de 20 minutes.
- [ ] Je sais expliquer en 1 phrase pourquoi FastAPI a besoin des type hints.
- [ ] Je sais expliquer en 1 phrase ce qu'un décorateur fait.
- [ ] Je sais pourquoi `except:` tout court est dangereux.
- [ ] Je n'utilise plus `os.path` ni la concaténation de strings pour les
      chemins — `pathlib.Path` partout.
- [ ] Je connais les 6 pièges listés et leurs symptômes.
