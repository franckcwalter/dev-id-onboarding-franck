# Ressources P0 — Acculturation IA et préparation de poste (promo Dev-id)

> Brief associé : **P0 — pré-démarrage**.
> Mode : individuel, asynchrone, 4 à 5 heures, à attaquer dès réception (pas d'échéance couperet).
> L'énoncé complet du brief est dans le [`README.md`](../README.md) à la racine de ce repo.

Ce dossier rassemble **toutes les ressources pédagogiques** auxquelles le brief P0
fait référence. Tu peux le parcourir dans n'importe quel ordre, mais l'ordre
suggéré ci-dessous t'évite de butter inutilement.

---

## 📚 Ordre de lecture suggéré

| # | Mini-cours | Durée | Quand le faire |
|---|---|---|---|
| 1 | [`01_Setup_environnement_essentiel.md`](./01_Setup_environnement_essentiel.md) | 1 h | **Tout au début** — sans poste qui marche, tu perds une demi-journée au démarrage |
| 2 | _Auto-évaluation Python_ — voir [`../squelette/Test_Positionnement_Python.ipynb`](../squelette/Test_Positionnement_Python.ipynb) | 30 min | Après le setup |
| 3 | [`00_Python_survival_kit.md`](./00_Python_survival_kit.md) | 60-90 min | **Conditionnel** — si tu as raté 2+ questions du bloc 1 du test OU tu n'as pas écrit de Python depuis longtemps OU tu débutes. Sinon, saute. |
| 4 | [`05_Python_essentiel.md`](./05_Python_essentiel.md) | 45 min | **Selon profil** — si tu n'es pas à l'aise avec décorateurs / type hints / context managers / `pathlib`. Sinon survol rapide. (Pré-requis : le kit de survie #3 si tu en as eu besoin.) |
| 5 | [`02_Numpy_essentiel.md`](./02_Numpy_essentiel.md) | 45 min ([voie A](#-deux-voies)) ou 5 min (voie B) | À ton rythme |
| 6 | [`03_Pandas_essentiel.md`](./03_Pandas_essentiel.md) | 45 min (voie A) ou 5 min (voie B) | Après NumPy |
| 7 | [`04_Acculturation_IA_essentiel.md`](./04_Acculturation_IA_essentiel.md) | 45 min — **obligatoire pour tout le monde** | Quand tu veux |
| 8 | _Produire ton notebook de présentation_ — squelette dans [`../squelette/presentation_template.ipynb`](../squelette/presentation_template.ipynb) | 1 h | À la fin |

---

## 🚦 Deux voies

Le brief P0 propose **2 voies** (cf. [`README.md`](../README.md) racine) :

- **Voie A — baseline** : tu suis tous les exercices guidés des mini-cours, tu
  utilises le squelette `presentation_template.ipynb` pour la mini-démo.
- **Voie B — avancée** : tu survoles NumPy / Pandas (lecture rapide pour repérer
  la stack imposée), tu produis ta propre mini-démo libre.

Quelle que soit ta voie : **acculturation IA + notebook qui tourne** sont
indispensables (ce sont les 2 signaux que la formatrice utilise pour te calibrer au démarrage).

---

## 🎯 Ce qu'on cherche à atteindre

À la fin de P0, tu dois :

- Avoir Python 3.11+, un env virtuel, un IDE, Git/GitHub fonctionnels.
- Savoir lancer Jupyter et écrire 10 lignes pandas sans paniquer.
- Pouvoir distinguer **supervisé / non supervisé / transfer learning / LLM** et
  argumenter quand un LLM est pertinent vs sur-dimensionné.
- T'auto-positionner sur ton **mur réflexif initial** sur l'IA.

---

## 🔗 Liens externes

Toutes les URLs externes utilisées dans les mini-cours sont consolidées dans
[`liens_officiels.md`](./liens_officiels.md), vérifiées avant chaque envoi de
brief par l'outillage formateur.

---

## 🆘 Bloqué·e ?

1. Relire la section concernée du mini-cours (chacun a un **exercice guidé** avec
   solution).
2. Tester l'**exemple minimal** du mini-cours (il est garanti fonctionnel).
3. Si rien n'y fait, envoyer un mail à la formatrice avec **ce que tu as essayé**
   (pas juste « ça marche pas »).

C'est un brief asynchrone : on prend le temps, et on déroule le reste ensemble au démarrage.