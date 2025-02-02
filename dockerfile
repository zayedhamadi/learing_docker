# 1. Utilisation d'une image de base Python
FROM python:3.9

# 2. Définition du répertoire de travail
WORKDIR /app

# 3. Copie du script serveur dans le conteneur
COPY server.py .

# 4. Définition de la commande par défaut pour démarrer le serveur
CMD ["python", "server.py"]
