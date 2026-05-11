import streamlit as st
import pandas as pd

# Titre de la page
st.title("🏪 Tableau de bord — Boutique chez YG")

# Sous-titre
st.subheader("Ventes du mois de mars 2026")

# Données simulées
data = {
    "Produit": ["Chaussures", "Maillots", "Shorts", "Casquettes", "Chaussettes"],
    "Quantité vendue": [42, 30, 55, 20, 80],
    "Prix unitaire (€)": [89, 45, 25, 15, 8],
}

df = pd.DataFrame(data)

# Calcul du chiffre d'affaires
df["CA (€)"] = df["Quantité vendue"] * df["Prix unitaire (€)"]

# Afficher le tableau
st.dataframe(df)

# Afficher un chiffre clé
total_ca = df["CA (€)"].sum()
st.metric(label="💰 Chiffre d'affaires total", value=f"{total_ca} €")

# Graphique simple
st.bar_chart(df.set_index("Produit")["CA (€)"])