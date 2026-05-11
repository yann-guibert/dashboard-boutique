import streamlit as st
import pandas as pd
from fpdf import FPDF

# ─── DONNÉES ───────────────────────────────────────────
data = {
    "Produit": ["Chaussures", "Maillots", "Shorts", "Casquettes", "Chaussettes", "Bijoux"],
    "Catégorie": ["Chaussures", "Vêtements", "Vêtements", "Accessoires", "Accessoires", "Accessoires"],
    "Quantité vendue": [42, 30, 55, 20, 80, 21],
    "Prix unitaire (€)": [89, 45, 25, 15, 8, 16],
}

df = pd.DataFrame(data)
df["CA (€)"] = df["Quantité vendue"] * df["Prix unitaire (€)"]

# ─── SIDEBAR ───────────────────────────────────────────
st.sidebar.title("🔧 Filtres")

categorie_choisie = st.sidebar.selectbox(
    "Catégorie :",
    options=["Toutes"] + list(df["Catégorie"].unique())
)

quantite_min = st.sidebar.slider(
    "Quantité minimum vendue :",
    min_value=0,
    max_value=100,
    value=0
)

# ─── FILTRES ───────────────────────────────────────────
if categorie_choisie != "Toutes":
    df = df[df["Catégorie"] == categorie_choisie]

df = df[df["Quantité vendue"] >= quantite_min]

# ─── TITRE ─────────────────────────────────────────────
st.title("🏪 Boutique Sport YG — Tableau de bord")
st.caption("Rapport mensuel — Mars 2026")

st.divider()

# ─── KPIs ──────────────────────────────────────────────
st.subheader("📊 Indicateurs clés")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 CA Total", f"{df['CA (€)'].sum()} €")

with col2:
    st.metric("📦 Produits", len(df))

with col3:
    st.metric("🏆 Meilleure vente", df.loc[df["CA (€)"].idxmax(), "Produit"])

st.divider()

# ─── TABLEAU ───────────────────────────────────────────
st.subheader("📋 Détail des ventes")
st.dataframe(df, use_container_width=True)

st.divider()

# ─── GRAPHIQUE ─────────────────────────────────────────
st.subheader("📈 Chiffre d'affaires par produit")
st.bar_chart(df.set_index("Produit")["CA (€)"])

st.divider()

# ─── EXPORT PDF ────────────────────────────────────────
st.subheader("📄 Export du rapport")

def generer_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Rapport Ventes - Boutique Sport YG", ln=True, align="C")
    pdf.cell(0, 10, "Mars 2026", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(60, 10, "Produit", border=1)
    pdf.cell(40, 10, "Qtt vendue", border=1)
    pdf.cell(40, 10, "Prix unitaire", border=1)
    pdf.cell(40, 10, "CA (euros)", border=1)
    pdf.ln()
    pdf.set_font("Helvetica", "", 10)
    for _, row in df.iterrows():
        pdf.cell(60, 10, str(row["Produit"]), border=1)
        pdf.cell(40, 10, str(row["Quantité vendue"]), border=1)
        pdf.cell(40, 10, str(row["Prix unitaire (€)"]), border=1)
        pdf.cell(40, 10, str(row["CA (€)"]), border=1)
        pdf.ln()
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, f"CA total : {df['CA (€)'].sum()} euros", ln=True)
    return bytes(pdf.output())

if st.button("📄 Générer le rapport PDF"):
    pdf_bytes = generer_pdf(df)
    st.download_button(
        label="⬇️ Télécharger le PDF",
        data=pdf_bytes,
        file_name="rapport_mars2026.pdf",
        mime="application/pdf"
    )