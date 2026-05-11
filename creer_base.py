import sqlite3
import pandas as pd

conn = sqlite3.connect("boutique.db")

data = {
    "Produit": ["Chaussures", "Maillots", "Shorts", "Casquettes", "Chaussettes", "Bijoux"],
    "Quantité vendue": [42, 30, 55, 20, 80, 21],
    "Prix unitaire": [89, 45, 25, 15, 8, 16],
}

df = pd.DataFrame(data)
df["CA"] = df["Quantité vendue"] * df["Prix unitaire"]

df.to_sql("ventes", conn, if_exists="replace", index=False)

print("Base créée !")
print(df.columns.tolist())
conn.close()
