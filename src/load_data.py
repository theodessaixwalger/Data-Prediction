# src/load_data.py
import pandas as pd

# Chemins des fichiers CSV
circuits_file = "../data/circuits.csv"
constructor_results_file = "../data/constructor_results.csv"
constructor_standings_file = "../data/constructor_standings.csv"

# Charger les datasets CSV
circuits = pd.read_csv(circuits_file)
constructor_results = pd.read_csv(constructor_results_file)
constructor_standings = pd.read_csv(constructor_standings_file)

# Afficher les 5 premières lignes pour vérifier
print("Circuits:\n", circuits.head(), "\n")
print("Constructor Results:\n", constructor_results.head(), "\n")
print("Constructor Standings:\n", constructor_standings.head(), "\n")
