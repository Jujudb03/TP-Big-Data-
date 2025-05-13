print('hello word')


#HOW  TO RUN STREAMLIT APP IN Anaconda Promt

import streamlit as st
#C:\Users\PC\Documents\Julien\ESTP\2A\Machine learning\JOUR jsp\Untitled-1.py
#streamlit run TP streamlit DI BATTISTA LAVERGNE.py

#1 PRESENTATION GENERALE
st.write("Hello, world! This is a Streamlit app.")
st.title("The Streamlit App Of DI BATTISTA")
st. subheader("Try out the app!")
st.text("This is a simple text element.")

#3 UPLOAD CSV FILE
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

# Choix dans une liste déroulante (dans la sidebar)
graph_type = st.selectbox("lil Choisissez un type de graphique :", ["Ligne", "Barres", "Aucun"])

st.write(f"Vous avez choisi le type de graphique : {graph_type}")



if uploaded_file is not None:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write("Voici un aperçu de votre fichier :")
    st.dataframe(df.head())

    #4 Affichage du graphique en fonction du type choisi
    if graph_type == "Ligne":
        st.line_chart(df)
    elif graph_type == "Barres":
        st.bar_chart(df)
    else:
        st.write("Aucun graphique selectionne.")

st.write("Merci d'avoir utilise notre application Streamlit !")


#4 SLider
age = st.slider("Quel âge avez-vous ?", 0, 100, 25)
st.write(f"Vous avez {age} ans.")

import pandas as pd
import numpy as np
# Checkbox
if st.checkbox("Afficher un tableau aleatoire"):
    st.write(pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']) )
