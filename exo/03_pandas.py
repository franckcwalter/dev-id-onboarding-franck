# Versions testées : python 3.11, pandas 2.x
import pandas as pd

# Petit dataset bidon
df = pd.DataFrame({
    "ville":   ["Paris", "Lyon", "Paris", "Marseille", "Lyon", "Paris"],
    "age":     [30, 25, 45, 28, 31, 22],
    "salaire": [42000, 38000, 65000, 35000, 41000, 30000],
    "tele":    [True, False, True, False, True, True],
})

# Inspection
print(df.head())
print()
print(df.info())
print()
print(df.describe(include="all"))

# Filtrage + sélection
print()
print(df[df["age"] > 28][["ville", "salaire"]])

# Groupby
print()
print(df.groupby("ville")["salaire"].mean().round(0))

# Petite visualisation (nécessite matplotlib)
df.groupby("ville")["salaire"].mean().plot.bar(title="Salaire moyen par ville")