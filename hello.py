import streamlit as st
from pathlib import Path

from modules.data.images import image_path
from modules.entries.add import add_project
from modules.entries.show import afficher_projets
from modules.data.load_data import load_markdown, load_html

from data.pages.capacites import capacites


def projets():
    st.html("to be done")

def accueil():
    load_markdown("data/pages/accueil.md")

def apropos():
    load_markdown("data/pages/apropos.md")

def lexique():
    load_html("data/pages/lexique.html")

page_names_to_func = {"Accueil": accueil, 
                      "Capacités de l'IA": capacites,
                      "Projets":afficher_projets,
                      "Lexique": lexique,
                      #"Ajouter un projet":add_project,
                      "À propos": apropos}

demo_name = st.sidebar.selectbox("Sélectionnez la page qui vous intéresse", page_names_to_func.keys(), index=0)
page_names_to_func[demo_name]()
