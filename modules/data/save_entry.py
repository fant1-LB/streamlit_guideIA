from pathlib import Path
import os
import json
import streamlit as st

def save_notice(json_project):
    dir_path = Path("data") / "projects_entries"
    dir_path.mkdir(parents=True, exist_ok=True)

    id_unique = json_project.get("id_unique")

    if not id_unique:
        st.error("ID unique manquant.")
        return

    path_project = dir_path / f"{id_unique}.json"

    if path_project.exists():
        st.error("Une notice avec cet UUID existe déjà.")
        return

    try:
        with open(path_project, "w", encoding="utf-8") as f:
            json.dump(json_project, f, ensure_ascii=False, indent=2)

        st.success("Projet sauvegardé avec succès.")

    except Exception as e:
        st.error(f"Erreur : {e}")
