import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard F1 Weather - Demo")

# Charger les fichiers clean
circuits = pd.read_csv("data/cleaned/circuits_clean.csv")
constructor_results = pd.read_csv("data/cleaned/constructor_results_clean.csv")
constructor_standings = pd.read_csv("data/cleaned/constructor_standings_clean.csv")
drivers = pd.read_csv("data/cleaned/drivers_clean.csv")
weahter = pd.read_csv("data/cleaned/F1_Weather_clean.csv")
# Afficher les datasets
st.header("Circuits")
st.dataframe(circuits)

st.header("Résultats des Constructors")
st.dataframe(constructor_results)

st.header("Classement des Constructors")
st.dataframe(constructor_standings)

st.header("Les drivers")
st.dataframe(drivers)

st.header("La météo")
st.dataframe(weahter)

# Exemple simple : filtrer les résultats d'un constructeur
constructor_id = st.selectbox("Choisir un constructorId :", constructor_results['constructorId'].unique())
filtered_results = constructor_results[constructor_results['constructorId'] == constructor_id]

st.subheader(f"Résultats pour le constructorId {constructor_id}")
st.dataframe(filtered_results)