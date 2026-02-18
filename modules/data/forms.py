import os
import json
from modules.data.load_data import load_data


DATA_DIR = "data"
LIST_FORM_DIR = os.path.join(DATA_DIR, "list_form")

LIST_FORM = {
    "fourche_financement":"fourchette_financement.json",
    "objet_etude": "objet_etude.json",
    "artists_roles": "artists_roles.json",
    "participants_types":"participants_types.json",
    "statut_projet": "statut_projet.json",
    "usages_ia": "usages_ia.json",
    "usages_pro": "usages_pro.json"
}

def load_list_form(*keys: str):
    seen = set()
    merged = []

    for key in keys:
        if key not in LIST_FORM:
            raise ValueError(f"Clé inconnue : {key}")

        path = os.path.join(LIST_FORM_DIR, LIST_FORM[key])

        data = load_data(path)
        if not isinstance(data, list):
            continue

        for item in data:
            if item not in seen:
                seen.add(item)
                merged.append(item)

    return sorted(merged)

def save_to_list_form(key: str, value):
    if key not in LIST_FORM:
        raise ValueError(f"Clé inconnue : {key}")

    # Normaliser value → toujours une liste
    if value is None:
        return

    if isinstance(value, str):
        values = [value]
    elif isinstance(value, list):
        values = value
    else:
        raise TypeError("value doit être une str ou une list")

    # Nettoyage : enlever None / chaînes vides / espaces
    values = [
        str(v).strip()
        for v in values
        if v is not None and str(v).strip() != ""
    ]

    if not values:
        return

    path = os.path.join(LIST_FORM_DIR, LIST_FORM[key])

    # Charger les données existantes
    data = load_data(path)

    if not isinstance(data, list):
        data = []

    # Ajouter uniquement les nouvelles valeurs
    updated = False
    for v in values:
        if v not in data:
            data.append(v)
            updated = True

    # Écriture uniquement si modification
    if updated:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(sorted(data), f, ensure_ascii=False, indent=2)

def sync_list_form(key: str, selected_values):
    """
    Compare les valeurs sélectionnées avec celles existantes
    et ajoute uniquement les nouvelles.
    """

    existing_values = load_list_form(key)

    if isinstance(selected_values, str):
        selected_values = [selected_values]

    if not isinstance(selected_values, list):
        return

    new_values = [
        v for v in selected_values
        if v not in existing_values and str(v).strip() != ""
    ]

    if new_values:
        save_to_list_form(key, new_values)