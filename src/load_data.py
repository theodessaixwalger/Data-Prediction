# src/load_data.py
import pandas as pd

# Chemins des fichiers CSV
circuits_file = "../data/circuits.csv"
constructor_results_file = "../data/constructor_results.csv"
constructor_standings_file = "../data/constructor_standings.csv"
constructors_file= "../data/constructors.csv"
driver_standings_file="../data/driver_standings.csv"
drivers_file="../data/drivers.csv"
weather_file='../data/F1_Weather.csv'
pit_stops_file="../data/pit_stops.csv"
qualifying_file="../data/qualifying.csv"
races_file="../data/races.csv"
results_file="../data/results.csv"
seasons_file="../data/seasons.csv"
sprint_results_file="../data/sprint_results.csv"
status_file="../data/status.csv"

# Charger les datasets CSV
circuits = pd.read_csv(circuits_file)
constructor_results = pd.read_csv(constructor_results_file)
constructor_standings = pd.read_csv(constructor_standings_file)
constructors=pd.read_csv(constructors_file)
driver_standings=pd.read_csv(driver_standings_file)
drivers=pd.read_csv(drivers_file)
weather=pd.read_csv(weather_file)
pit_stops=pd.read_csv(pit_stops_file)
qualifying=pd.read_csv(qualifying_file)
races=pd.read_csv(races_file)
results=pd.read_csv(results_file)
seasons=pd.read_csv(seasons_file)
sprint_results=pd.read_csv(sprint_results_file)
status=pd.read_csv(status_file)

# Afficher les 5 premières lignes pour vérifier
print("Circuits:\n", circuits.head(), "\n")
print("Constructor Results:\n", constructor_results.head(), "\n")
print("Constructor Standings:\n", constructor_standings.head(), "\n")
print("Constructor :\n", constructors.head(), "\n")
print("Driver Standings :\n", driver_standings.head(), "\n")
print("Driver :\n", drivers.head(), "\n")
print("Weahter :\n", weather.head(), "\n")
print("Pit stops :\n", pit_stops.head(), "\n")
print("Qualifying :\n", qualifying.head(), "\n")
print("Races :\n", races.head(), "\n")
print("Results :\n", results.head(), "\n")
print("Seasons :\n", seasons.head(), "\n")
print("Sprint results :\n", sprint_results.head(), "\n")
print("Status :\n", status.head(), "\n")