# src/clean_data.py
import pandas as pd

# Charger les fichiers CSV bruts
circuits = pd.read_csv("../data/circuits.csv")
constructor_results = pd.read_csv("../data/constructor_results.csv")
constructor_standings = pd.read_csv("../data/constructor_standings.csv")
constructors=pd.read_csv("../data/constructors.csv")
driverstand=pd.read_csv("../data/driver_standings.csv")
drivers=pd.read_csv('../data/drivers.csv')
#weather=pd.read_csv('../F1_Weather.csv')
pitstops=pd.read_csv('../data/pit_stops.csv')
qualifying=pd.read_csv('../data/qualifying.csv',na_values='\\N')
races=pd.read_csv('../data/races.csv')
results=pd.read_csv('../data/results.csv',na_values='\\N')
seasons=pd.read_csv('../data/seasons.csv')
sprintresults=pd.read_csv('../data/sprint_results.csv')
status=pd.read_csv('../data/status.csv')

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

# Fonction pour nettoyer constructors
def clean_constructors(df):
    columns_to_keep = [col for col in ['constructorId', 'constructorRef'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer drivers
def clean_driver(df):
    columns_to_keep = [col for col in ['driverId', 'driverRef'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer drivers stranding
def clean_driver_standing(df):
    columns_to_keep = [col for col in ['raceId', 'driverId','points','position','wins'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer weather
#def clean_weather(df):
    columns_to_keep = [col for col in ['AirTemp', 'Humidity','Rainfall','TrackTemp','WindSpeed','Pressure'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer pit_stops
def clean_pit_stops(df):
    columns_to_keep = [col for col in ['raceId', 'driverId', 'time'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer qualifying
def clean_qualifying(df):
    columns_to_keep = [col for col in ['qualifyId','raceId', 'driverId', 'constructorId','position','q1','q2','q3'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer races
def clean_races(df):
    columns_to_keep = [col for col in ['qualifyId','raceId', 'driverId', 'constructorId','position','q1','q2','q3'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer results
def clean_results(df):
    columns_to_keep = [col for col in ['grid','position', 'points', 'laps','fastestLapTime','fastestLapSpeed','statusId'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer seasons
def clean_seasons(df):
    columns_to_keep = [col for col in ['year'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer sprint results
def clean_sprint_result(df):
    columns_to_keep = [col for col in ['raceId','constructorId','grid','position','laps','milliseconds','fatestLapTime','points'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Fonction pour nettoyer status
def clean_status(df):
    columns_to_keep = [col for col in ['statusId','status'] if col in df.columns]
    df = df[columns_to_keep]
    df = df.dropna()
    return df

# Appliquer les nettoyages
circuits_clean = clean_circuits(circuits)
constructor_results_clean = clean_constructor_results(constructor_results)
constructor_standings_clean = clean_constructor_standings(constructor_standings)
constructors_clean=clean_constructors(constructors)
driversstand_clean=clean_driver_standing(driverstand)
drivers_clean=clean_driver(drivers)
#weather_clean=clean_weather(weather)
pitstops_clean=clean_pit_stops(pitstops)
qualifying_clean=clean_qualifying(qualifying)
races_clean=clean_races(races)
results_clean=clean_results(results)
seasons_clean=clean_seasons(seasons)
sprintresults_clean=clean_sprint_result(sprintresults)
status_clean=clean_status(status)

# Sauvegarder dans data/cleaned
circuits_clean.to_csv("../data/cleaned/circuits_clean.csv", index=False)
constructor_results_clean.to_csv("../data/cleaned/constructor_results_clean.csv", index=False)
constructor_standings_clean.to_csv("../data/cleaned/constructor_standings_clean.csv", index=False)
constructors_clean.to_csv("../data/cleaned/constructors_clean.csv", index=False)
driversstand_clean.to_csv("../data/cleaned/drivers_standings_clean.csv", index=False)
drivers_clean.to_csv("../data/cleaned/drivers_clean.csv", index=False)
#weather_clean.to_csv("../data/cleaned/F1_Weather_clean.csv", index=False)
pitstops_clean.to_csv("../data/cleaned/pit_stops_clean.csv", index=False)
qualifying_clean.to_csv("../data/cleaned/qualifying_clean.csv", index=False)
races_clean.to_csv("../data/cleaned/races_clean.csv", index=False)
results_clean.to_csv("../data/cleaned/results_clean.csv", index=False)
seasons_clean.to_csv("../data/cleaned/seasons_clean.csv", index=False)
sprintresults_clean.to_csv("../data/cleaned/sprint_results_clean.csv", index=False)
status_clean.to_csv("../data/cleaned/status_clean.csv", index=False)
print("Nettoyage terminé et fichiers sauvegardés dans data/cleaned !")
