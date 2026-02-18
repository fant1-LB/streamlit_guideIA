import os
import json
from pathlib import Path

def load_data(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

PAGES_DIR = Path("data") / "pages"
PAGES_NAMES = {
    "accueil" : "accueil.html",
    "lexique" : "lexique.html"
}

def load_html(page_key):
    """Charge le contenu HTML à partir d'une clé du dictionnaire PAGES_NAMES."""
    # On récupère le nom du fichier grâce à la clé
    filename = PAGES_NAMES.get(page_key)
    
    if filename:
        file_path = PAGES_DIR / filename
        return file_path.read_text(encoding="utf-8")
    
    raise KeyError(f"La clé '{page_key}' n'existe pas dans PAGES_NAMES.")