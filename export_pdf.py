import streamlit as st
import pandas as pd
from fpdf import FPDF

# Données de la boutique
data = {
    "Produit": ["Chaussures", "Maillots", "Shorts", "Casquettes", "Chaussettes", "Bijoux"],
    "Quantité vendue": [42, 30, 55, 20, 80, 21],
    "Prix unitaire (€)": [89, 45, 25, 15, 8, 16],
}

df = pd.DataFrame(data)
df["CA (€)"] = df["Quantité vendue"] * df["Prix unitaire (€)"]

# Titre
st.title("🏪 Tableau de bord — Boutique Sport YG")
st.subheader("Ventes du mois de mars 2026")

# Afficher le tableau
st.dataframe(df)

# KPIs
total_ca = df["CA (€)"].sum()
st.metric(label="💰 Chiffre d'affaires total", value=f"{total_ca} €")

# Fonction qui génère le PDF
def generer_pdf(df, total_ca):
    pdf = FPDF()
    pdf.add_page()
    
    # Titre
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Rapport Ventes - Boutique Sport YG", ln=True, align="C")
    pdf.cell(0, 10, "Mars 2026", ln=True, align="C")
    pdf.ln(10)
    
    # En-têtes du tableau
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(60, 10, "Produit", border=1)
    pdf.cell(40, 10, "Qtt vendue", border=1)
    pdf.cell(40, 10, "Prix unitaire", border=1)
    pdf.cell(40, 10, "CA (euros)", border=1)
    pdf.ln()
    
    # Lignes du tableau
    pdf.set_font("Helvetica", "", 10)
    for _, row in df.iterrows():
        pdf.cell(60, 10, str(row["Produit"]), border=1)
        pdf.cell(40, 10, str(row["Quantité vendue"]), border=1)
        pdf.cell(40, 10, str(row["Prix unitaire (€)"]), border=1)
        pdf.cell(40, 10, str(row["CA (€)"]), border=1)
        pdf.ln()
    
    # Total
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, f"Chiffre d'affaires total : {total_ca} euros", ln=True)
    
    return bytes(pdf.output())

# Bouton de téléchargement
if st.button("📄 Générer le rapport PDF"):
    pdf_bytes = generer_pdf(df, total_ca)
    st.download_button(
        label="⬇️ Télécharger le PDF",
        data=pdf_bytes,
        file_name="rapport_boutique_mars2026.pdf",
        mime="application/pdf"
    )