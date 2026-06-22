# Squelette — `presentation_<prénom>.ipynb`

Ce dossier contient le squelette du livrable P0.

## Comment l'utiliser

1. Renomme `presentation_template.ipynb` en `presentation_<ton-prénom>.ipynb`.
2. Place-le à la racine de ton repo `dev-id-onboarding-<prénom>` créé en Tâche 1 du brief.
3. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   # ▸ Env créé avec uv ? (uv venv n'embarque pas pip) → uv pip install -r requirements.txt
   ```
4. Ouvre Jupyter, complète les 6 sections, **vérifie que tout tourne** sans erreur.
5. Commit, push.

## Contenu

| Fichier | Rôle |
|---|---|
| `presentation_template.ipynb` | Trame du notebook livrable, 6 sections à compléter |
| `requirements.txt` | Dépendances minimales (pandas, matplotlib, jupyter) |
| `.gitignore` | À copier à la racine de ton repo si tu n'en as pas déjà |

## Vérification finale

Avant de pousser :

- [ ] Le notebook a un nom `presentation_<prenom>.ipynb` (pas `Untitled.ipynb`)
- [ ] **Toutes les cellules** ont été exécutées dans l'ordre, dans une session propre
      (`Kernel > Restart & Run All`)
- [ ] Aucune cellule ne renvoie d'erreur
- [ ] Le `.gitignore` exclut `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`, `.env`
- [ ] Le repo est public **ou** la formatrice a un accès lecture