**🥗 Tasty Bytes : Optimisation du trafic des recettes**
Ce projet est une solution de Data Science visant à prédire la popularité des recettes pour le site "Tasty Bytes". En automatisant la sélection des recettes pour la page d'accueil, nous maximisons l'engagement des utilisateurs et les abonnements premium.

**🚀 Fonctionnalités principales**
Nettoyage automatisé : Traitement des valeurs manquantes et normalisation des données nutritionnelles.

Pipeline ML : Utilisation de scikit-learn avec une LogisticRegression optimisée pour une haute précision (83.65% de précision sur les recettes à fort trafic).

API haute performance : Interface RESTful via FastAPI permettant une intégration facile.

Déploiement conteneurisé : Système entièrement Dockerisé pour une portabilité totale.

**🛠 Architecture du projet**
Plaintext
tasty-bytes-project/
├── app/             # API FastAPI
├── models/          # Modèles entraînés (.joblib)
├── src/             # Logique de traitement et d'entraînement
├── data/            # Données sources (non versionnées)
├── Dockerfile       # Configuration du conteneur
└── requirements.txt # Dépendances Python

**⚙️ Installation locale**
Clonez le dépôt :

```Bash
git clone https://github.com/sefimiakanda/tasty-bytes-project.git
cd tasty-bytes-optimizer
Créez un environnement virtuel et installez les dépendances :

Bash
python -m venv venv
source venv/bin/activate  # Ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
Exécutez l'API localement :

```Bash
uvicorn app.main:app --reload

**🐳 Utilisation avec Docker**
Pour construire et lancer l'image localement :

Bash
docker build -t tasty-bytes-app .
docker run -p 8000:8000 tasty-bytes-app

**📈 Monitoring**
Le système enregistre chaque prédiction dans un fichier predictions.log pour permettre une analyse du comportement des utilisateurs et détecter toute dérive du modèle (Data Drift).

**👤 Auteur**
Fidèle Miakanda, Division Data Science : Tasty Bytes.