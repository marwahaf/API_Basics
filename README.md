# API Basics

**Note :** Ce projet est avant tout à des fins éducatives personnelles. Mon objectif est uniquement de comprendre le fonctionnement des API.

Une **API** (Interface de Programmation d'Applications) permet à deux systèmes informatiques de communiquer entre eux. Cela est utile pour automatiser des tâches telles que l'envoi de rapports par email via un service comme Gmail. Par exemple, un script Python peut appeler l'API de Gmail pour envoyer un message avec un rapport, sans intervention humaine.

### Principales parties d'une API

#### 1. Protocoles HTTP
Le protocole HTTP est la méthode principale pour la communication sur le web. Voici les méthodes courantes utilisées dans une API :

- **GET** : Obtient des informations d'une base de données ou d'un processus.
  *Exemple* : Récupérer des données d'un utilisateur.
  
- **POST** : Envoie des informations à l'API.
  *Exemple* : Soumettre un formulaire de contact ou envoyer des données d'une analyse.

- **PUT** : Met à jour des informations existantes dans une base de données.
  *Exemple* : Modifier les informations d'un utilisateur.

- **DELETE** : Supprime des informations.
  *Exemple* : Supprimer un compte utilisateur.

#### 2. URL et Endpoints

Une API est accessible via une **URL** (Uniform Resource Locator). L'URL se compose de trois parties :

- **Protocole** : `http://` ou `https://`
- **Domaine** : L'adresse du serveur où l'API est hébergée (par exemple, `localhost` ou un domaine externe).
- **Endpoint** : La partie de l'URL qui spécifie l'action ou la ressource demandée. Par exemple, `http://127.0.0.1:8000/items/5`.

Chaque **endpoint** est conçu pour effectuer des actions spécifiques, comme obtenir ou envoyer des données.

---

# FastAPI

FastAPI est un framework moderne et rapide pour créer des API avec Python. Il est basé sur **Starlette** pour les parties réseau et sur **Pydantic** pour la validation des données. Il est conçu pour être simple à utiliser tout en étant très performant.

### Lancer le serveur FastAPI

Pour démarrer le serveur FastAPI, utilise la commande suivante (assure-toi d'avoir installé les dépendances au préalable) :

```bash
uvicorn fastapi_main:app --reload
```

Cette commande démarre le serveur localement et permet de recharger le code à chaque modification. Dans le terminal, tu verras une ligne du genre :

```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Cela indique l'URL où l'API est accessible sur ta machine locale.

### Test de l'API

Dans ton navigateur, lance l'une des URL suivantes pour tester l'API :

- `http://localhost:8000/?name=Marwa`  
- `http://localhost:8000/`  
- `http://127.0.0.1:8000/items/5?q=somequery`

Ces URL sont liées à différents **endpoints** de l'API que nous avons créés.

### Fonctionnalités de l'API :

- Gestion des requêtes HTTP pour les chemins `/` et `/items/{item_id}`, en supportant les opérations GET pour les deux.
- Le chemin `/items/{item_id}` inclut un paramètre requis `item_id` de type **int** et un paramètre optionnel `q` de type **str**. Si `q` n'est pas fourni, il prend la valeur par défaut `None`.
- Validation du `item_id` dans les requêtes GET et PUT, avec des messages d'erreur clairs si ce paramètre n'est pas valide.
- Pour les requêtes PUT sur `/items/{item_id}`, le corps de la requête doit inclure :
  - Un attribut **name** de type **str** (requis).
  - Un attribut **price** de type **float** (requis).
  - Un attribut **is_offer** de type **bool** (facultatif).
- Conversion automatique des données entre **JSON** et **objets Python**.
- Génération de la documentation OpenAPI, permettant :
  - Exploration interactive de l'API.
  - Génération automatique du code client pour différents langages.
- Documentation interactive disponible à ces adresses :
  - Swagger UI : `http://127.0.0.1:8000/docs`
  - ReDoc : `http://127.0.0.1:8000/redoc`

---

# Générer un certificat SSL auto-signé

Lorsque nous exécutons une API en production ou même en développement, il est important de sécuriser les échanges avec un **SSL** (Secure Sockets Layer). Cela chiffre les données entre le serveur et le client.

Voici comment générer un certificat SSL auto-signé pour un environnement local :

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
```

Cela génère deux fichiers : `cert.pem` pour le certificat et `key.pem` pour la clé privée. Ces fichiers peuvent être utilisés pour configurer l'API avec HTTPS, assurant ainsi une communication sécurisée.

---

# Flask

Flask est un autre framework Python pour la création d'API. Il fonctionne de manière similaire à FastAPI, mais avec une syntaxe différente. Bien que FastAPI soit plus moderne et offre des fonctionnalités avancées comme la validation automatique des données, Flask est une alternative légère et flexible.

### Lancer le serveur Flask

Pour démarrer le serveur Flask, utilise la commande suivante :

```bash
python flask_main.py
```

Flask ne requiert pas d'installation de serveur externe (comme **Uvicorn** pour FastAPI), mais offre une approche simple pour commencer à développer des API en Python.

---

# Conclusion

En résumé, la création d'APIs avec **FastAPI** et **Flask** est relativement simple. Cependant, chaque framework a ses avantages :

- **FastAPI** : Très rapide, avec validation automatique des données et génération de documentation interactive. Idéal pour les projets nécessitant des API modernes et robustes.
- **Flask** : Plus simple, flexible et léger, mais nécessite plus de configuration manuelle, notamment pour la validation des données et la documentation.

Le choix dépend de tes besoins spécifiques. Si tu cherches une solution prête à l'emploi avec des fonctionnalités intégrées, FastAPI est un excellent choix. Si tu préfères une solution plus légère et flexible, Flask pourrait être plus adapté.

---

### Récapitulatif des commandes :

- Pour démarrer FastAPI :
  ```bash
  uvicorn fastapi_main:app --reload
  ```

- Pour démarrer Flask :
  ```bash
  python flask_main.py
  ```

- Pour générer un certificat SSL auto-signé :
  ```bash
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
  ```

