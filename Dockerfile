# Utiliser une image Python officielle et légère
FROM python:3.10-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances dans le conteneur
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source
COPY . .

# Exposer le port sur lequel l'API tourne
EXPOSE 8000

# Commande pour démarrer l'API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]