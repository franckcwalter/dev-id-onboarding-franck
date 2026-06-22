# P0 — Acculturation IA et préparation de poste (promo Dev-id)

> **Brief de pré-démarrage — promo Dev-id.**
> Durée : **4 à 5 heures**, à ton rythme.
> Modalité : individuel, asynchrone. **Non évalué** (préparation).
>
> ⚠️ Ce brief t'est envoyé **la veille du démarrage**. Dans l'idéal :
> 1. **Ce soir / dès réception** → priorité absolue à la **Tâche 1 (poste opérationnel)**.
>    Si Python / Git / Jupyter ne tournent pas chez toi au démarrage, tu perds une
>    demi-journée pendant que les autres avancent.
> 2. **Le reste** (mini-cours, notebook de présentation) se complète dans les
>    **premiers jours** de la formation. On fait le point ensemble au démarrage.

Tout ce dont tu as besoin est **dans ce repo** : l'énoncé (ci-dessous), les
mini-cours (`ressources/`) et le squelette de code (`squelette/`). Aucun autre
outil n'est requis pour démarrer.

---

## 🚀 Démarrage en 4 commandes

1. Clique sur **« Use this template »** en haut de ce repo → crée ton repo perso
   `dev-id-onboarding-<prénom>` (public, ou en lecture pour la formatrice).
2. Clone-le et installe l'environnement :

```bash
git clone <url-de-ton-repo-perso>
cd dev-id-onboarding-<prénom>
python -m venv .venv && source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r squelette/requirements.txt
# ▸ Si tu as créé l'env avec uv (uv venv n'embarque pas pip) :
#   uv pip install -r squelette/requirements.txt
```

3. Ouvre le squelette du notebook : `jupyter notebook squelette/presentation_template.ipynb`
4. Travaille, commit chez toi, et envoie le **lien de ton repo** à la formatrice par mail.

> Détail complet de l'installation (IDE, Git, vérifications) :
> [`ressources/01_Setup_environnement_essentiel.md`](./ressources/01_Setup_environnement_essentiel.md).

---

## 🎬 Situation professionnelle

> **FastIA, l'ESN qui te recrute.**
>
> Bienvenue chez **FastIA**, ESN polyvalente qui prend des missions IA chez des clients
> de l'industrie, de la banque, de la santé, du public. Tu rejoins l'équipe « Conception
> et intégration IA » qui livre des solutions de bout en bout : analyse du besoin,
> préparation des données, modélisation, déploiement, monitoring.
>
> **Ton manager t'écrit la veille de ton premier jour :**
>
> > « Salut,
> > avant de démarrer, prépare ton poste et fais un point sur tes acquis. Comme tu sais,
> > on est sur des missions IA mais on ne demande pas à nos profils IT d'être data
> > scientists. En revanche, on attend que tu sois à l'aise avec un environnement
> > Python moderne, que tu saches lire un notebook Jupyter et faire tourner un
> > modèle, et que tu aies le vocabulaire de base pour parler à nos data scientists
> > sans que ça grince.
> >
> > Tu trouveras dans le repo d'onboarding ce qu'il faut lire et faire. Renvoie-moi
> > dès que tu peux un petit notebook qui me permet de voir où tu en es : qui tu es,
> > ce que tu attends de la mission, et un mini-script qui charge un fichier CSV
> > et sort un graphique. Pas plus. On en parlera au démarrage.
> >
> > À très vite,
> > Karim, manager FastIA. »

C'est ce notebook que tu vas produire dans ce brief.

---

## 🚀 Profil avancé en Python data ? Tu as 2 voies possibles

| Tu es… | Voie suggérée |
|---|---|
| **Débutant·e ou pas à l'aise** en Python data | **Voie A** : suivre les 5 tâches dans l'ordre, faire les exercices guidés des mini-cours NumPy / Pandas, utiliser le squelette imposé pour la mini-démo. C'est l'objectif baseline. |
| **Expérimenté·e** (≥ 2 ans de pandas / numpy quotidien) | **Voie B** : **survoler** les mini-cours NumPy / Pandas (lecture de 5 min, pas les exercices), et **produire ta propre mini-démo libre** à la place du squelette (cf. section 4 du livrable). |

💡 **Garde-fou — quelle que soit ta voie, 2 signaux sont indispensables** :

1. Les **3 réponses acculturation IA rédigées par toi** (tâche 4).
2. Un **notebook qui tourne sans erreur** (section 4 du livrable).

Sans ces 2 signaux, je ne peux pas calibrer ton démarrage.

---

## 🎯 Objectifs pédagogiques

À la fin de ce brief, tu seras capable de :

1. Disposer d'un environnement Python 3.11+ fonctionnel avec un IDE et Git configurés.
2. Cloner un repo, installer ses dépendances, lancer un notebook Jupyter.
3. Manipuler des structures de données de base avec **NumPy** et **Pandas**
   (chargement, sélection, agrégation simple, premier graphique).
4. Distinguer les grandes familles de l'IA (apprentissage supervisé, non supervisé,
   apprentissage par transfert, foundation models, LLM) et identifier dans quelle famille
   se range un cas d'usage donné.
5. T'auto-positionner sur ton mur réflexif initial (« qu'est-ce que je sais déjà ?
   qu'est-ce qui est flou ? »).

> ⚠️ **Ce brief n'est pas évalué pour la certification.** C'est une préparation. En revanche
> ton livrable est attendu pour que je puisse calibrer le démarrage et adapter le tutorat.

---

## 🗓️ Modalités

| Élément | Détail |
|---|---|
| Durée totale | **4 à 5 heures** |
| Format | Individuel, asynchrone |
| Période | **Dès réception.** Poste opérationnel pour le démarrage ; le reste sur les premiers jours. Pas d'échéance couperet. |
| Outils | Python 3.11+, IDE (VS Code, PyCharm Community ou autre), Git, GitHub |
| Livrable | 1 notebook Jupyter `presentation_<prénom>.ipynb` (cf §Livrable) |
| Canal de rendu | Lien GitHub (repo perso public ou avec accès lecture pour la formatrice) — par mail |

---

## 🧰 Tâches

### Tâche 1 — Préparer ton poste (≈ 1 h) — **à faire en premier, dès ce soir**

Lis le mini-cours [`ressources/01_Setup_environnement_essentiel.md`](./ressources/01_Setup_environnement_essentiel.md)
et exécute la procédure jusqu'à ce que tu obtiennes le résultat « validation »
(`python --version` + un notebook qui s'ouvre + un commit Git réussi).

### Tâche 2 — Auto-évaluation Python (≈ 30 min)

Le notebook [`squelette/Test_Positionnement_Python.ipynb`](./squelette/Test_Positionnement_Python.ipynb)
est fourni dans `squelette/`. Réponds aux 12 questions auto-corrigées.
**Tu n'es pas obligé·e de tout réussir.** L'objectif est juste de me donner un signal
pour adapter le démarrage et calibrer ton tutorat individuel.

Pousse le notebook complété sur **ton repo GitHub** aux côtés du notebook de présentation.

### Tâche 3 — Numpy + Pandas en mode survol pratique (≈ 1 h 30)

Pour chacun des deux mini-cours :

- [`ressources/02_Numpy_essentiel.md`](./ressources/02_Numpy_essentiel.md)
- [`ressources/03_Pandas_essentiel.md`](./ressources/03_Pandas_essentiel.md)

**Voie A** (Python data débutant·e) → lis le mini-cours en mode actif (15-20 min)
puis fais l'exercice guidé.

**Voie B** (avancé·e) → survole en lecture rapide pour repérer la stack imposée
(versions, conventions de nommage, sklearn pipelines). Skip les exercices.

L'objectif baseline n'est pas de tout retenir, c'est de **manipuler une fois**
chaque outil pour ne pas le découvrir au démarrage.

### Tâche 4 — Acculturation IA (≈ 45 min)

Lis [`ressources/04_Acculturation_IA_essentiel.md`](./ressources/04_Acculturation_IA_essentiel.md).
À la fin, tu dois pouvoir répondre par écrit (3-5 lignes chacune) à :

- Qu'est-ce qui distingue **apprentissage supervisé** et **apprentissage non supervisé** ?
- À quoi sert le **transfer learning** ? Donne un exemple.
- Pourquoi un **LLM n'est pas toujours la bonne réponse** à un problème métier ?

Tu intègres tes réponses dans le notebook livrable (section dédiée).

> 💬 Ces 3 réponses seront **discutées collectivement au démarrage** — pas de notation,
> juste une mise en perspective de la pluralité des formulations.

### Tâche 5 — Produire le notebook de présentation (≈ 1 h)

Cf. § Livrable ci-dessous.

---

## 📦 Livrable

**Un seul notebook** : `presentation_<prénom>.ipynb`, poussé sur ton GitHub dans un
repo personnel `dev-id-onboarding-<prénom>` (public ou en lecture pour la formatrice).

Structure imposée du notebook (le squelette est fourni dans
[`squelette/presentation_template.ipynb`](./squelette/presentation_template.ipynb)) :

1. **Qui suis-je** (5 lignes) — parcours pro court, secteur, ce qui t'amène ici.
2. **Mon mur réflexif initial sur l'IA** — 3-4 phrases, sans filtre, sur ce qui est
   clair / flou / mystère pour toi quand on dit « IA ». **C'est l'amorce du mur
   réflexif collaboratif** installé au démarrage — tu pourras la faire évoluer toute
   la formation.
3. **Ce que j'attends de cette formation** — 3-4 phrases, attentes pro et perso.
4. **Mini-démo technique** — au choix selon ta voie :
   - **Voie A** (baseline) : reprends le squelette fourni dans
     [`squelette/presentation_template.ipynb`](./squelette/presentation_template.ipynb),
     charge le CSV **Penguins**, affiche `df.head()` / `df.describe()`, produis
     1 graphique matplotlib simple commenté.
   - **Voie B** (avancé·e) : **démo libre** sur un dataset public non-bateau
     (pas Iris, pas Titanic, pas Boston Housing). Contraintes :
     - chargement d'un dataset (CSV / Parquet / API publique)
     - **au moins 3 opérations** Pandas (groupby, jointure, pivot, fenêtre, etc.)
     - **au moins 1 graphique** matplotlib / seaborn / plotly commenté
     - 1 phrase d'observation analytique sur ce que tu montres
5. **Réponses aux 3 questions d'acculturation IA** (cf. tâche 4).
6. **Une question que je veux poser à la formatrice** dès le démarrage.

---

## ✅ Critères de performance

**Communs aux 2 voies :**
- Le notebook **s'ouvre et tourne sans erreur** avec une version Python 3.11+.
- Le repo GitHub contient un `.gitignore` correct (pas de `.venv`, pas de `__pycache__`).
- Le notebook respecte la structure imposée (les 6 sections).
- Les **3 réponses d'acculturation IA** sont rédigées par toi (pas du copier-coller
  de Wikipédia ou ChatGPT).
- La question pour la formatrice est précise (pas « j'ai plein de questions »).

**Spécifique voie A** (baseline) :
- Section 4 : tu as utilisé le squelette Penguins, avec `df.head()`, `df.describe()`,
  1 graphique commenté en 1 ligne.

**Spécifique voie B** (avancé·e) :
- Section 4 : ≥ 3 opérations Pandas, ≥ 1 graphique commenté, 1 phrase d'observation.
- Tu **indiques en début de section 4 « Voie B »** pour que je sache te lire correctement.

---

## 🎓 Compétences visées

**Aucune compétence CISIA évaluée** — brief préparatoire.

Compétences transversales mobilisées :
- Recherche d'informations en autonomie
- Reproductibilité d'un environnement de dev
- Communication écrite synthétique

---

## 📚 Ressources

Toutes les ressources nécessaires sont dans [`ressources/`](./ressources/) :

| Fichier | Quand l'ouvrir |
|---|---|
| [`01_Setup_environnement_essentiel.md`](./ressources/01_Setup_environnement_essentiel.md) | Tâche 1 |
| [`00_Python_survival_kit.md`](./ressources/00_Python_survival_kit.md) | Conditionnel (si Python rouillé) |
| [`05_Python_essentiel.md`](./ressources/05_Python_essentiel.md) | Selon profil |
| [`02_Numpy_essentiel.md`](./ressources/02_Numpy_essentiel.md) | Tâche 3 |
| [`03_Pandas_essentiel.md`](./ressources/03_Pandas_essentiel.md) | Tâche 3 |
| [`04_Acculturation_IA_essentiel.md`](./ressources/04_Acculturation_IA_essentiel.md) | Tâche 4 |
| [`liens_officiels.md`](./ressources/liens_officiels.md) | À tout moment |

Squelette de départ pour le notebook livrable :
[`squelette/presentation_template.ipynb`](./squelette/presentation_template.ipynb)

Avant d'envoyer ton rendu, passe la checklist d'auto-évaluation :
[`verification/checklist_apprenant.md`](./verification/checklist_apprenant.md)

---

## 🆘 En cas de blocage

1. Relire la section concernée du mini-cours.
2. Tester l'exemple minimal du mini-cours (il est garanti fonctionnel).
3. Si toujours bloqué : envoyer un mail à la formatrice en précisant **ce que tu as
   essayé** (pas juste « ça marche pas ») et le message d'erreur exact.

C'est un brief asynchrone : on prend le temps, et on déroule le reste ensemble au démarrage.
