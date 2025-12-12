## Description
Ce projet vise à extraire automatiquement des **règles métiers** depuis des documents PDF (procédures, normes, rapports) en utilisant une approche **neuro-symbolique** (OCR + NLP + ontologies).

## Structure du Projet
NS_A/                      # Racine du projet
│
├── data/                  # Données brutes et traitées
│   ├── raw/               # PDF originaux (ne pas modifier)
│   ├── processed/         # Textes extraits, JSON, CSV
│   └── cache/             # Cache des extractions OCR
│
├── docs/                  # Documentation (schémas, décisions d'architecture)
│   ├── architecture.md    # Description de l'architecture
│   └── user_guide.md      # Guide pour les utilisateurs
│
├── src/                   # Code source (logique métier)
│   ├── ocr/               # Modules liés à l'OCR
│   │   ├── __init__.py
│   │   ├── pdf_processor.py  # Détection de type, extraction
│   │   ├── image_preprocessing.py  # Pré-traitement des images
│   │   └── utils.py        # Fonctions utilitaires (nettoyage, logs)
│   │
│   ├── neo4j/             # Intégration avec Neo4j
│   │   ├── __init__.py
│   │   ├── schema.py       # Définition du schéma Neo4j
│   │   ├── queries.py      # Requêtes Cypher pré-défines
│   │   └── connector.py    # Connexion et opérations de base
│   │
│   ├── rules/             # Gestion des règles métiers
│   │   ├── __init__.py
│   │   ├── extractor.py    # Extraction de règles depuis le texte
│   │   ├── validator.py    # Validation des règles avec les experts
│   │   └── ontology.py     # Gestion de l'ontologie
│   │
│   ├── interfaces/         # Interfaces utilisateur
│   │   ├── __init__.py
│   │   ├── streamlit_app.py  # Interface de validation
│   │   └── cli.py          # Ligne de commande pour les scripts
│   │
│   └── main.py             # Point d'entrée principal
│
├── tests/                 # Tests unitaires et d'intégration
│   ├── __init__.py
│   ├── test_ocr.py        # Tests pour les modules OCR
│   ├── test_neo4j.py      # Tests pour les requêtes Neo4j
│   └── test_rules.py      # Tests pour l'extraction de règles
│
├── scripts/               # Scripts utilitaires (non destinés à la production)
│   ├── convert_pdfs.py    # Conversion de PDF en images
│   ├── generate_ontology.py # Génération initiale de l'ontologie
│   └── cleanup_data.py    # Nettoyage des données
│
├── config/                # Fichiers de configuration
│   ├── neo4j_config.yaml  # Paramètres de connexion à Neo4j
│   ├── ocr_config.yaml    # Paramètres OCR (langues, seuils)
│   └── logging_config.yaml # Configuration des logs
│
├── requirements.txt        # Dépendances Python (pip)
├── requirements-dev.txt    # Dépendances pour le développement (tests, linting)
├── pyproject.toml          # Configuration moderne (poetry, black, mypy)
├── README.md               # Documentation principale
└── .gitignore              # Fichiers à ignorer par Git


## Prérequis
- Python 3.11+
- Neo4j (version 5.x)
- Tesseract OCR (pour `pytesseract`)

## Installation
```bash
pip install -r requirements.txt


## utilisation de interfaces/cli 
python -m src.interfaces.cli extract data/raw/procedure.pdf data/processed/procedure.json


