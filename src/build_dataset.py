import pandas as pd
import os

# === Charger fichiers nettoyés ===
races = pd.read_csv("../data/cleaned/races_clean.csv")
circuits = pd.read_csv("../data/cleaned/circuits_clean.csv")
results = pd.read_csv("../data/cleaned/results_clean.csv")
drivers = pd.read_csv("../data/cleaned/drivers_clean.csv")
constructors = pd.read_csv("../data/cleaned/constructors_clean.csv")
qualifying = pd.read_csv("../data/cleaned/qualifying_clean.csv")
weather = pd.read_csv("../data/cleaned/F1_Weather_clean.csv")
status = pd.read_csv("../data/cleaned/status_clean.csv")

# === Étape 1 : Résultats principaux ===
df = results.merge(races, on="raceId", how="left") \
            .merge(circuits, on="circuitId", how="left") \
            .merge(drivers, on="driverId", how="left") \
            .merge(constructors, on="constructorId", how="left")

# === Étape 2 : Position en qualifications ===
df = df.merge(
    qualifying[["raceId", "driverId", "position"]],
    on=["raceId", "driverId"],
    how="left",
    suffixes=("", "_Quali")
)

# === Étape 3 : Statuts (abandon, accident, etc.) ===
df = df.merge(status, on="statusId", how="left")

# === Étape 4 : Harmoniser et joindre la météo ===
weather = weather.rename(columns={"Year": "year", "Round Number": "round"})

# Convertir en int pour éviter les mismatches
df["year"] = df["year"].astype(int)
df["round"] = df["round"].astype(int)
weather["year"] = weather["year"].astype(int)
weather["round"] = weather["round"].astype(int)

df = df.merge(weather, on=["year", "round"], how="left")

# === Étape 5 : Filtrer 2018-2023 ===
df = df[(df["year"] >= 2018) & (df["year"] <= 2023)]

# === Sauvegarder dataset final ===
output_dir = "../data/final"
os.makedirs(output_dir, exist_ok=True)

df.to_csv(os.path.join(output_dir, "f1_dataset.csv"), index=False)
print("✅ Dataset final filtré (2018-2023) créé dans data/final/f1_dataset.csv")
