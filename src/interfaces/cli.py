import click
from src.ocr.pdf_processor import process_pdf
from src.rules.extractor import extract_rules

@click.group()
def cli():
    """Outil en ligne de commande pour le projet NS_A."""
    pass

@cli.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def extract(input_path: str, output_path: str):
    """Extrait le texte et les règles d'un PDF."""
    text, tables, pdf_type = process_pdf(input_path)
    rules = extract_rules(text)

    with open(output_path, "w") as f:
        import json
        json.dump({"text": text, "rules": rules}, f, indent=2)
    click.echo(f"Extraction terminée. Résultats sauvegardés dans {output_path}")

if __name__ == "__main__":
    cli()
