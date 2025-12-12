from src.ocr.pdf_processor import process_pdf
from src.rules.extractor import extract_rules
from src.neo4j.connector import Neo4jConnector
from src.rules.validator import validate_rules
import os

def process_directory(input_dir: str, output_dir: str, n: int):
    """Traite tous les PDF d'un dossier."""
    connector = Neo4jConnector()
    for pdf_file in os.listdir(input_dir)[:n]:
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, pdf_file)
            text, tables, pdf_type = process_pdf(pdf_path)



            # Extraire les règles
            rules = extract_rules(text)

            # Valider les règles (interface Streamlit ou CLI)
            validated_rules = validate_rules(rules)

            # Stocker dans Neo4j
            connector.store_rules(validated_rules)

            # Sauvegarder les résultats
            output_path = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}.json")
            with open(output_path, "w") as f:
                import json
                json.dump({"text": text, "rules": rules}, f)

if __name__ == "__main__":
    process_directory("data/raw/", "data/processed/", 1)
