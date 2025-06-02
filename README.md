# MLOps - Prédiction Iris

Application de prédiction des classes de fleurs d'Iris utilisant un modèle XGBoost déployé avec FastAPI et une interface Streamlit.

## Architecture

- **Server** : API FastAPI servant un modèle XGBoost
- **Client** : Interface web Streamlit
- **Déploiement** : Docker Compose

## Structure

```
├── server/
│   ├── app.py          # API FastAPI
│   ├── train.py        # Entraînement du modèle
│   └── modelXGBoost.pkl
├── client/
│   └── app.py          # Interface Streamlit
└── docker-compose.yml
```

## Utilisation

### Démarrage rapide

```bash
git clone https://github.com/QL2111/mlops_iris.git
cd mlops_iris
```

```bash
docker-compose up --build
```

### Accès
- **Interface utilisateur** : http://localhost:8501
- **API** : http://localhost:8000/redoc

## Fonctionnalités

- Prédiction en temps réel des classes d'Iris
- Interface web intuitive
- API REST documentée
- Déploiement containerisé

## Technologies

- **ML** : XGBoost, scikit-learn
- **Backend** : FastAPI, Uvicorn
- **Frontend** : Streamlit
- **Containerisation** : Docker

## Auteur
**Auteur : Quentin LIM**  
Université Lyon 2  
[GitHub](https://github.com/QL2111)
