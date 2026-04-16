import os
import json
from pathlib import Path
import streamlit as st

def load_data(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    

def load_html(path: str):
    """
    Charge et affiche un fichier HTML.
    
    :param path: chemin vers le fichier HTML
    """
    file_path = Path(path)
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        st.markdown(content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Fichier introuvable : {file_path}")

def load_markdown(path: str):
    """
    Charge et affiche un fichier markdown.
    
    :param section: nom du dossier (ex: "ressources")
    :param filename: nom du fichier sans extension (ex: "liens")
    """
    file_path = Path(path)
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        st.markdown(content)
    except FileNotFoundError:
        st.error(f"Fichier introuvable : {file_path}")