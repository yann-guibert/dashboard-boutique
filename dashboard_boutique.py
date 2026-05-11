import streamlit as st
import pandas as pd

# Titre de la page
st.title("🏪 Tableau de bord — Boutique Sport YG")

# Sous-titre
st.subheader("Ventes du mois de mars 2026")

# Données simulées
data = {
    "Produit": ["Chaussures", "Maillots", "Shorts", "Casquettes", "Chaussettes", "Bijoux"],
    "Quantité vendue": [42, 30, 55, 20, 80, 21],
    "Prix unitaire (€)": [89, 45, 25, 15, 8,16],
}

df = pd.DataFrame(data)

# Calcul du chiffre d'affaires
df["CA (€)"] = df["Quantité vendue"] * df["Prix unitaire (€)"]

# Menu déroulant pour filtrer par produit
produit_choisi = st.sidebar.selectbox (
    "Choisir un produit :",
    options=["Tous les produits"] + list(df["Produit"])
)

# Filtrer le DataFrame selon le choix
if produit_choisi != "Tous les produits":
    df = df[df["Produit"] == produit_choisi]

# Afficher le tableau
st.dataframe(df)

# Slider pour filtrer par quantité minimum vendue
quantite_min = st.sidebar.slider(
    "Quantité minimum vendue :",
    min_value=0,
    max_value=100,
    value=0
)

# Appliquer le filtre quantité
df = df[df["Quantité vendue"] >= quantite_min]

# Afficher un chiffre clé
total_ca = df["CA (€)"].sum()
st.metric(label="💰 Chiffre d'affaires total", value=f"{total_ca} €")
st.metric(label="📦 Produits différents", value=len(df))

# Graphique simple
st.bar_chart(df.set_index("Produit")["CA (€)"])