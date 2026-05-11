import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("boutique.db")
df = pd.read_sql("SELECT * FROM ventes", conn)
conn.close()

st.title("🏪 Tableau de bord — Boutique Sport YG (SQL)")
st.subheader("Ventes du mois de mars 2026")

produit_choisi = st.sidebar.selectbox(
    "Choisir un produit :",
    options=["Tous les produits"] + list(df["Produit"])
)

quantite_min = st.sidebar.slider(
    "Quantité minimum vendue :",
    min_value=0,
    max_value=100,
    value=0
)

if produit_choisi != "Tous les produits":
    df = df[df["Produit"] == produit_choisi]

df = df[df["Quantité vendue"] >= quantite_min]

st.dataframe(df)

total_ca = df["CA"].sum()
st.metric(label="💰 Chiffre d'affaires total", value=f"{total_ca} €")
st.metric(label="📦 Produits différents", value=len(df))

st.bar_chart(df.set_index("Produit")["CA"])