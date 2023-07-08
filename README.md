# Spotify-Data-API-with-ETL-Pipeline

### English version 

In this project, I successfully built an ETL (Extract, Transform, Load) data pipeline using Python to gather data from the Spotify public API. The pipeline involves extracting data about a desired artist, transforming and validating the data, and loading it into a PostgreSQL database table. By leveraging the Spotify Developer platform, I created a developer account, generated the necessary credentials (Client ID and Client Secret), and built a Python project consisting of a main.py file and a package called service. The service package contains separate Python files for the extraction, transformation/validation, and loading phases. To ensure secure handling of sensitive information, I stored the Client ID, Client Secret, and database password in a .env file and utilized the dotenv library to manage environment variables.

1. Created a developer account on Spotify and generated a Client ID and Client Secret.
2. Built a Python project with a main.py file and a service package for extraction, transformation/validation, and loading.
3. Stored sensitive information (Client ID, Client Secret, and database password) in a secure .env file using the dotenv library.
4. Extracted data about a desired artist from the Spotify API and loaded it as a JSON object.
5. Parsed the JSON object into a Pandas DataFrame, extracting the "song_name" and "album_name" columns.
6. Validated the DataFrame to remove duplicates and null values.
7. Loaded the validated data into a PostgreSQL database table.
8. Completed an efficient ETL pipeline, successfully extracting, transforming, and loading the artist's songs data into the database.


### French version
Dans ce projet, j'ai réussi à construire un pipeline de données ETL (Extract, Transform, Load) en utilisant Python pour collecter des données à partir de l'API publique de Spotify. Le pipeline implique l'extraction de données sur un artiste spécifique, la transformation et la validation des données, puis le chargement dans une table de base de données PostgreSQL. En exploitant la plateforme Spotify Developer, j'ai créé un compte développeur, généré les identifiants nécessaires (ID client et secret client), et construit un projet Python composé d'un fichier main.py et d'un package appelé service. Le package service contient des fichiers Python distincts pour les phases d'extraction, de transformation/validation et de chargement. Afin de garantir une gestion sécurisée des informations sensibles, j'ai stocké l'ID client, le secret client et le mot de passe de la base de données dans un fichier .env sécurisé et j'ai utilisé la bibliothèque dotenv pour gérer les variables d'environnement.

1. Création d'un compte développeur sur Spotify et génération d'un ID client et d'un secret client.
2. Construction d'un projet Python comprenant un fichier main.py et un package service pour les phases d'extraction, de transformation/validation et de chargement.
3. Stockage des informations sensibles (ID client, secret client et mot de passe de la base de données) dans un fichier .env sécurisé en utilisant la bibliothèque dotenv.
4. Extraction des données d'un artiste spécifique à partir de l'API Spotify et chargement des données sous forme d'objet JSON.
5. Analyse de l'objet JSON pour extraire les colonnes "song_name" et "album_name" et conversion en DataFrame Pandas.
6. Validation du DataFrame pour éliminer les doublons et les valeurs nulles.
7. Chargement des données validées dans une table de base de données PostgreSQL.
8. Achèvement d'un pipeline ETL efficace, avec succès dans l'extraction, la transformation et le chargement des données des chansons de l'artiste dans la base de données.
