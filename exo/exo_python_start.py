# Refactorez le script ci-dessous (style « junior pressé ») en code idiomatique mobilisant les 5 concepts.

from pathlib import Path
from functools import wraps

from exo.demo_python import log_call



def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"-> appel {func.__name__}({args},{kwargs})")
        result = func(*args, **kwargs)
        print(f"<- retour {result!r}")
        return result
    return wrapper


@log_call
def predire(surf: float, nb: int) -> float:
    return 4500 * surf + 12000 * nb

def charger(p:Path)-> str:
    try:
        with p.open("r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError :
        print("file not found")
        return ""

if __name__ == "__main__":
    data_dir = Path("data")
    file_path = data_dir / "input.txt"
    data = charger(file_path)
    print(data)
    prix = predire(65, 3)
    print(f"prix = {prix}")

