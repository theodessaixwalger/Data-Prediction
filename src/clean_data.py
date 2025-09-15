# src/clean_data.py
import pandas as pd

# Charger les fichiers CSV bruts
circuits = pd.read_csv("../data/circuits.csv")
constructor_results = pd.read_csv("../data/constructor_results.csv")
constructor_standings = pd.read_csv("../data/constructor_standings.csv")

# Fonction pour nettoyer circuits
def clean_circuits(df):
    columns_to_keep = [col for col in ['circuitId', 'name', 'location', 'country'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer constructor_results
def clean_constructor_results(df):
    columns_to_keep = [col for col in ['raceId', 'constructorId', 'points', 'position', 'positionOrder'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer constructor_standings
def clean_constructor_standings(df):
    columns_to_keep = [col for col in ['constructorId', 'points', 'position', 'positionOrder'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Appliquer les nettoyages
circuits_clean = clean_circuits(circuits)
constructor_results_clean = clean_constructor_results(constructor_results)
constructor_standings_clean = clean_constructor_standings(constructor_standings)

# Sauvegarder dans data/cleaned
circuits_clean.to_csv("../data/cleaned/circuits_clean.csv", index=False)
constructor_results_clean.to_csv("../data/cleaned/constructor_results_clean.csv", index=False)
constructor_standings_clean.to_csv("../data/cleaned/constructor_standings_clean.csv", index=False)

print("Nettoyage terminé et fichiers sauvegardés dans data/cleaned !")
