import os
from neo4j import GraphDatabase
import detect_pdf as ipdf 


# Configuration Neo4j (optionnel)
driver = GraphDatabase.driver("bolt://localhost:7688", auth=("neo4j", "votre_mot_de_passe_securise"))

# Dossier contenant les 12 PDF
pdf_dir = "../data/raw"
processed = []


def store_in_neo4j(text, pdf_path, driver):
    def add_document(tx, text, path):
        tx.run("""
        CREATE (d:Document {
            path: $path,
            content: $text,
            extracted_at: datetime()
        })
        """, path=pdf_path, text=text)

    with driver.session() as session:
        session.execute_write(add_document, text, pdf_path)


for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        print("pdf_path :",pdf_path)
        try:
            # Détecter le type de PDF
            pdf_type = ipdf.detect_pdf_type(pdf_path)

            # Extraire le texte
            if pdf_type == "native_text":
                text = ipdf.extract_text_native(pdf_path)
            elif pdf_type == "scanned":
                text = ipdf.extract_text_scanned(pdf_path)
            else:
                text, tables = ipdf.extract_complex_pdf(pdf_path)

            # Nettoyer le texte
            clean_text = ipdf.clean_text(text)

            # Stocker dans Neo4j (optionnel)
            store_in_neo4j(clean_text, pdf_path, driver)

            # Ajouter aux résultats
            processed.append({
                "file": pdf_file,
                "type": pdf_type,
                "content": clean_text,
                "tables": tables if pdf_type == "complex" else None
            })
            print(f"Traitement terminé pour {pdf_file} (Type: {pdf_type})")

        except Exception as e:
            print(f"Échec pour {pdf_file}: {str(e)}")
            processed.append({
                "file": pdf_file,
                "error": str(e)
            })

# Résumé des résultats
print("\n=== Résumé des Extractions ===")
for doc in processed:
    print(f"- {doc['file']}: {'Succès' if 'content' in doc else 'Échec'}")
