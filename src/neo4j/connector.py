# src/neo4j/connector.py
from neo4j import GraphDatabase
from src.config.loader import get_neo4j_config
import logging

class Neo4jConnector:
    """Classe pour gérer la connexion et les requêtes Neo4j."""

    def __init__(self):
        config = get_neo4j_config()
        self._uri = config["uri"]
        self._user = config["user"]
        self._password = config["password"]
        self._database = config.get("database", "neo4j")
        self._driver = None

    @property
    def driver(self):
        """Retourne le driver Neo4j (avec connexion lazy)."""
        if self._driver is None:
            self._driver = GraphDatabase.driver(
                self._uri,
                auth=(self._user, self._password)
            )
        return self._driver

    def close(self):
        """Ferme la connexion."""
        if self._driver is not None:
            self._driver.close()
            self._driver = None

    def execute_query(self, query: str, **params):
        """Exécute une requête Cypher."""
        with self.driver.session(database=self._database) as session:
            result = session.run(query, **params)
            return [dict(record) for record in result]

# Exemple d'utilisation
if __name__ == "__main__":
    connector = Neo4jConnector()
    try:
        result = connector.execute_query("MATCH (n) RETURN n LIMIT 5")
        print(result)
    finally:
        connector.close()
