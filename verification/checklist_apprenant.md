# Checklist apprenant — P0 (promo Dev-id)

> À parcourir **avant d'envoyer ton livrable** à la formatrice.

## Poste de travail

- [ ] J'ai Python 3.11 ou plus récent installé.
- [ ] J'ai un environnement virtuel activé pour ce projet (un seul gestionnaire, cf. mini-cours setup).
- [ ] J'ai installé les libs : `pandas`, `numpy`, `matplotlib`, `jupyter`.
- [ ] Je sais lancer `jupyter notebook` depuis mon terminal et ouvrir mon notebook.

## Git / GitHub

- [ ] J'ai créé mon repo perso via **« Use this template »** : `dev-id-onboarding-<prénom>`.
- [ ] Le repo est public **ou** la formatrice a un accès lecture.
- [ ] Mon `.gitignore` exclut `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`, `.env`.
- [ ] Mon historique Git contient au moins 2 commits avec des messages corrects
      (`type(scope): description`).

## Livrable — `presentation_<prénom>.ipynb`

- [ ] Le notebook s'appelle `presentation_<prénom>.ipynb`, **pas** `Untitled.ipynb`.
- [ ] J'ai fait `Kernel > Restart & Run All` : aucune cellule en erreur.
- [ ] **Section 1** (Qui suis-je) : 5 lignes max, claire.
- [ ] **Section 2** (Mur réflexif initial) : honnête, pas un copier-coller LinkedIn.
- [ ] **Section 3** (Attentes formation) : 3-4 phrases concrètes.
- [ ] **Section 4** (Mini-démo technique) — au choix selon ta voie :
  - **Voie A** (baseline avec squelette Penguins) :
    - [ ] CSV Penguins chargé via `pd.read_csv(URL)`
    - [ ] `df.head()` et `df.describe()` exécutés
    - [ ] 1 graphique matplotlib affiché
    - [ ] 1 ligne de commentaire sous le graphique (« on observe que… »)
  - **Voie B** (avancé·e — démo libre) :
    - [ ] Mention « Voie B » en début de section 4
    - [ ] Dataset chargé (non bateau : pas Iris, pas Titanic, pas Boston)
    - [ ] **≥ 3 opérations Pandas** (groupby, jointure, pivot, fenêtre, etc.)
    - [ ] **≥ 1 graphique** matplotlib / seaborn / plotly commenté
    - [ ] 1 phrase d'observation analytique
- [ ] **Section 5** (3 réponses acculturation IA) :
  - [ ] 5.1 supervisé / non supervisé
  - [ ] 5.2 transfer learning
  - [ ] 5.3 LLM pas toujours la bonne réponse
  - [ ] Réponses **rédigées par moi**, pas du copier-coller.
- [ ] **Section 6** (Question pour la formatrice) : 1 seule question, précise.

## Auto-évaluation Python

- [ ] J'ai répondu aux 12 questions du `squelette/Test_Positionnement_Python.ipynb`.
- [ ] Le notebook complété est **poussé sur mon repo GitHub** aux côtés du notebook
      de présentation.

## Mini-cours mobilisés

- [ ] J'ai fait l'exercice guidé du mini-cours **Setup environnement** (commun aux 2 voies).
- **Voie A uniquement** :
  - [ ] J'ai fait les 4 questions de l'exercice **NumPy**.
  - [ ] J'ai fait les 6 questions de l'exercice **Pandas** sur Penguins.
- **Voie B uniquement** :
  - [ ] J'ai survolé NumPy et Pandas pour repérer la stack imposée (versions, conventions).
- [ ] J'ai lu le mini-cours **Acculturation IA** et je peux citer 2 cas d'usage où
      un LLM est pertinent + 2 cas où c'est une mauvaise idée (commun aux 2 voies).

## Envoi

- [ ] J'envoie un mail à la formatrice avec :
  - [ ] Le **lien** vers mon repo GitHub (qui contient les 2 notebooks : présentation
        + positionnement Python rempli)
  - [ ] **2 lignes** de commentaire libre (« j'ai galéré sur X », « je me sens prêt sur Y »)

> Pas d'échéance couperet : ce brief t'arrive la veille du démarrage. Priorité au **poste
> opérationnel** dès maintenant ; le reste se complète dans les premiers jours, on en parle ensemble.
