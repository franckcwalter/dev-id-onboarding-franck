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
    RuntimeError
