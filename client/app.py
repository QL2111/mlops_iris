import streamlit as st
import requests
import numpy as np

# Définir l'URL du serveur FastAPI où le modèle est hébergé
SERVER_URL = "http://server:8000/predict"

# Personnalisation de l'interface utilisateur
st.set_page_config(
    page_title="Prédiction de Fleur d'Iris",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Titre et description
st.title("🌸 Prédiction de Fleur d'Iris")

st.write("Cette application prédit la classe d'une fleur d'Iris en fonction de ses caractéristiques.")
st.image("pokemon_meme.jpeg", caption="pokemon meme", use_container_width=True)

# Champs de saisie pour les caractéristiques
st.write("Entrez les caractéristiques de la fleur :")
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("🌿 Longueur du Sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
    petal_length = st.number_input("🌸 Longueur du Pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)

with col2:
    sepal_width = st.number_input("🌿 Largeur du Sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
    petal_width = st.number_input("🌸 Largeur du Pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Bouton pour effectuer la prédiction
if st.button("✨ Prédire la Classe"):
    # Préparer les données d'entrée
    features = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    # Envoyer les données d'entrée au serveur FastAPI pour la prédiction
    response = requests.post(SERVER_URL, json=features)

    # Afficher les résultats
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"🌟 Classe prédite : **{prediction}**")
    else:
        st.error("❌ Échec de la prédiction. Veuillez vérifier le serveur.")