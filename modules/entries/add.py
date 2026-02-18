import datetime
import streamlit as st
import json
import uuid

from modules.data.save_entry import save_notice
from modules.data.forms import load_list_form, sync_list_form
from modules.data.images import is_valid_url

def add_project():

    st.title("Création d'un projet")

    # -------------------------
    # ID
    # -------------------------
    projet_id = st.text_input("ID de la notice")

    if not projet_id:
        st.warning("Avant de commencer, veuillez donner un identifiant à votre notice")
        return

    # -------------------------
    # Champs simples
    # -------------------------
    titre_projet = st.text_input("Titre du projet")

    # -------------------------
    # Listes
    # -------------------------
    methodes_IA = st.multiselect(
        "Méthodes / usages de l'IA",
        load_list_form("usages_ia"),
        accept_new_options=True,
    )

    sync_list_form("usages_ia", methodes_IA)

    usage_pro = st.multiselect(
        "Usages professionnels",
        load_list_form("usages_pro"),
        accept_new_options=True,
    )

    sync_list_form("usages_pro", usage_pro)

    objet_etude = st.multiselect(
        "Objet d'étude",
        load_list_form("objet_etude"),
        accept_new_options=True,
    )

    sync_list_form("objet_etude", objet_etude)

    # -------------------------
    # Participants
    # -------------------------
    st.subheader("Participants")
    nb_participants = st.number_input("Nombre de participants", min_value=1, value=1)

    participants = []
    for i in range(nb_participants):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Nom", key=f"participant_nom_{i}")
        with col2:
            type_participant = st.selectbox("Type", load_list_form("participants_types"),key=f"participant_type_{i}", accept_new_options=True)
            sync_list_form("participants_types", type_participant)

        participants.append({
            "name": name,
            "type": type_participant
        })

    # -------------------------
    # Financement
    # -------------------------
    st.subheader("Financement")

    fourchette = st.selectbox("Fourchette", ["A", "B", "C"])
    valeur_secrete = st.text_input("Valeur approximative (secrète)")

    montant_financement = {
        "fourchette": fourchette,
        "valeur_approximative_secrete": valeur_secrete
    }

    # -------------------------
    # Dates
    # -------------------------
    st.subheader("Dates du projet")
    nb_dates = st.number_input("Nombre de dates", min_value=1, value=1)

    dates = []
    for i in range(nb_dates):

        col1, col2, col3 = st.columns([1, 1, 3])

        with col1:
            date_value = st.date_input(
                "Date",
                key=f"date_{i}"
            )

        with col2:
            type_date = st.selectbox(
                "Type",
                ["début du projet", "jalon", "fin du projet"],
                key=f"type_{i}"
            )

        with col3:
            date_text = st.text_input(
                "Description",
                key=f"text_{i}"
            )

        dates.append({
            "id_date": str(i),
            "date": date_value.isoformat(),
            "type": type_date,
            "date_text": date_text
        })

    # -------------------------
    # Statut
    # -------------------------
    statut = st.selectbox("Statut", ["en cours", "terminé"], index=None)
    livrable_statut = st.selectbox(
        "Livrable",
        ["livrable non disponible", "livrable disponible"],
        index=None
    )

    statut_projet = {
        "statut": statut,
        "livrable": livrable_statut
    }

    # -------------------------
    # Autres champs
    # -------------------------
    source_financement = st.text_area("Sources de financement (une par ligne)").splitlines()
    nbr_personnes_impliques = st.text_input("Nombre de personnes impliquées")

    quantite_donnees = st.text_area("Quantité de données (une par ligne)").splitlines()

    puissance_calcul_interne = st.checkbox("Puissance de calcul interne")
    ingenierie_interne = st.checkbox("Ingénierie interne")

    livrables = st.text_area("Livrables (un par ligne)").splitlines()

    # -------------------------
    # Ressources
    # -------------------------
    st.subheader("Ressources")
    nb_ressources = st.number_input("Nombre de ressources", min_value=0, value=0)

    ressources = []
    for i in range(nb_ressources):
        col1, col2 = st.columns(2)
        with col1:
            titre = st.text_input("Titre ressource", key=f"res_titre_{i}")
        with col2:
            url = st.text_input("URL", key=f"res_url_{i}")

        ressources.append({
            "titre": titre,
            "url": url
        })

    # -------------------------
    # Contacts
    # -------------------------
    st.subheader("Contacts")
    nb_contacts = st.number_input("Nombre de contacts", min_value=0, value=0)

    contacts = []
    for i in range(nb_contacts):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom contact", key=f"contact_nom_{i}")
        with col2:
            email = st.text_input("Email", key=f"contact_email_{i}")

        contacts.append({
            "nom": nom,
            "email": email
        })

    # -------------------------
    # Description & illustration
    # -------------------------
    description = st.text_area("Description du projet")

    show_image = False

    colIll1, colIll2 = st.columns([4, 1])
    with colIll1:
        illustration = st.text_input("URL de l'illustration")
    with colIll2:
        if illustration and illustration.strip():
            show_image = st.checkbox("Montrer l'image")
    
    if show_image:
        if is_valid_url(illustration):
            try:
                st.image(illustration)
            except Exception:
                st.warning("Impossible d'afficher l'image.")
        else:
            st.warning("URL invalide.")


    notice_termine = st.checkbox("Notice terminée")

    # -------------------------
    # Construction JSON final
    # -------------------------



    projet_json = {
        "id": projet_id,
        "titre_projet": titre_projet,
        "participants": participants,
        "methodes_IA": methodes_IA,
        "usage_pro": usage_pro,
        "objet_etude": objet_etude,
        "montant_financement": montant_financement,
        "dates": dates,
        "statut_projet": statut_projet,
        "source_financement": source_financement,
        "nbr_personnes_impliques": nbr_personnes_impliques,
        "quantite_donnees": quantite_donnees,
        "puissance_calcul_interne": puissance_calcul_interne,
        "ingenierie_interne": ingenierie_interne,
        "livrables": livrables,
        "ressources": ressources,
        "description": description,
        "contacts": contacts,
        "illustration": illustration,
        "notice_termine": notice_termine,
    }

    # -------------------------
    # Export & sauvegarde
    # -------------------------
    if st.button("Sauvegarder la notice"):
        id_unique = str(uuid.uuid4())

        # Reconstruire le dict avec id_unique en premier
        projet_json = {
            "id_unique": id_unique,
            **projet_json  # déplie le reste après
        }

        save_notice(projet_json)

    # -------------------------
    # Affichage
    # -------------------------
    st.divider()
    st.subheader("JSON généré")
    st.json(projet_json)