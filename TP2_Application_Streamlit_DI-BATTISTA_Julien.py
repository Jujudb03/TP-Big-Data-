# TP2 - Application Streamlit
# Nom : DI BATTISTA
# Prénom : Julien
# Lien de l'application : https://gkzobx7hmmqinb2mxf7m8d.streamlit.app
# https://github.com/Jujudb03/TP-Big-Data-/blob/main/TP2_Application_Streamlit_DI-BATTISTA_Julien.py


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Titanic Explorer", layout="centered")

# Titre
st.title("🚢 Analyse des données Titanic")

# 1. Saisie du prénom
name = st.text_input("Quel est ton prénom ?")
if name:
    st.success(f"Bienvenue à bord, {name} !")

# 2. Chargement des données (depuis le CSV fourni dans le dépôt ou via uploader)
uploaded_file = st.file_uploader("Charge le fichier Titanic (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # 3. Aperçu
    st.subheader("Aperçu du dataset")
    st.dataframe(df.head())

    # 4. Graphique simple : Répartition des survivants
    st.subheader("🔍 Répartition des survivants")
    surv_counts = df['Survived'].value_counts().rename({0: "Non Survivants", 1: "Survivants"})
    st.bar_chart(surv_counts)

    # 5. Corrélation entre colonnes numériques
    st.subheader("📊 Corrélations entre variables")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if len(numeric_cols) >= 2:
        corr = df[numeric_cols].corr()
        st.dataframe(corr)
    else:
        st.info("Pas assez de colonnes numériques pour afficher les corrélations.")

    # 6. Bonus : Graphique interactif avec Plotly
    st.subheader("📈 Scatter plot interactif")
    x_axis = st.selectbox("Variable X :", df.columns)
    y_axis = st.selectbox("Variable Y :", df.columns)
    fig = px.scatter(df, x=x_axis, y=y_axis, color="Survived", title=f"{y_axis} en fonction de {x_axis}")
    st.plotly_chart(fig)

    # 7. Bonus : Filtrage par âge avec un slider
    if "Age" in df.columns:
        st.subheader("🎚️ Filtrer les passagers selon l'âge")
        min_age = int(df["Age"].min())
        max_age = int(df["Age"].max())
        age_range = st.slider("Sélectionne une tranche d'âge", min_age, max_age, (min_age, max_age))
        filtered_df = df[(df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])]
        st.write(f"Nombre de passagers dans cette tranche : {filtered_df.shape[0]}")
        st.dataframe(filtered_df)
