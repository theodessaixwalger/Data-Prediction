import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard F1 Weather", layout="wide")
st.title("🏎️ Dashboard F1 - Influence de la météo et du circuit")

df = pd.read_csv("data/final/f1_dataset.csv")
df = df.dropna(subset=["driverId", "constructorId", "year", "round", "positionOrder",
                       "points", "Rainfall", "driverRef", "constructorRef", "name_x"])

st.sidebar.header("⚙️ Filtres")

# Filtre années
selected_years = st.sidebar.multiselect(
    "Choisir années :",
    options=sorted(df["year"].unique()),
    default=sorted(df["year"].unique())
)

# Filtre pilotes
selected_driver = st.sidebar.multiselect(
    "Choisir pilotes :",
    options=sorted(df["driverRef"].unique()),
    default=None
)

# Filtre constructeurs
selected_constructor = st.sidebar.multiselect(
    "Choisir constructeurs :",
    options=sorted(df["constructorRef"].unique()),
    default=None
)

# Filtre circuits
selected_circuit = st.sidebar.multiselect(
    "Choisir circuits :",
    options=sorted(df["name_x"].unique()),
    default=None
)

# Application des filtres
filtered_df = df[df["year"].isin(selected_years)]

if selected_driver:
    filtered_df = filtered_df[filtered_df["driverRef"].isin(selected_driver)]

if selected_constructor:
    filtered_df = filtered_df[filtered_df["constructorRef"].isin(selected_constructor)]

if selected_circuit:
    filtered_df = filtered_df[filtered_df["name_x"].isin(selected_circuit)]

# GRAPHIQUE 1 : Impact de la pluie sur les performances des pilotes
st.header("🌧️ Performances pilotes sous la pluie")

rain_df = filtered_df.copy()
rain_df["Rain"] = rain_df["Rainfall"].apply(lambda x: "Pluie" if x > 0 else "Sec")

avg_positions = rain_df.groupby(["driverRef", "Rain"])["positionOrder"].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=avg_positions, x="driverRef", y="positionOrder", hue="Rain", ax=ax)
ax.set_title("Position moyenne des pilotes (pluie vs sec)")
ax.set_ylabel("Position moyenne")
ax.set_xlabel("Pilote")
plt.xticks(rotation=90)
st.pyplot(fig)

# GRAPHIQUE 2 : Impact de la météo sur les constructeurs
st.header("🏎️ Performances des constructeurs selon la météo")

avg_points = rain_df.groupby(["constructorRef", "Rain"])["points"].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=avg_points, x="constructorRef", y="points", hue="Rain", ax=ax)
ax.set_title("Points moyens des constructeurs (pluie vs sec)")
ax.set_ylabel("Points moyens")
ax.set_xlabel("Constructeur")
plt.xticks(rotation=90)
st.pyplot(fig)

# GRAPHIQUE 3 : Influence du circuit
st.header("🗺️ Influence des circuits sur les performances")

circuit_perf = filtered_df.groupby(["name_x", "driverRef"])["points"].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=circuit_perf, x="name_x", y="points", ax=ax)
ax.set_title("Distribution des points par circuit")
ax.set_ylabel("Points")
ax.set_xlabel("Circuit")
plt.xticks(rotation=90)
st.pyplot(fig)

# GRAPHIQUE 4 : Evolution des performances dans le temps
st.header("📈 Evolution des performances par année")

yearly_perf = filtered_df.groupby(["year", "driverRef"])["points"].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=yearly_perf, x="year", y="points", hue="driverRef", marker="o", ax=ax)
ax.set_title("Points moyens par pilote au fil des années")
ax.set_ylabel("Points moyens")
ax.set_xlabel("Année")
st.pyplot(fig)

#Ajouter d'autres graphiques selon température, vitesse du vent, etc.
