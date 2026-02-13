import datetime
import streamlit as st
import json

def add_project():

    st.title("Création d'un projet")

    # --- Champs simples ---
    projet_id = st.text_input("ID de la notice")

    if not projet_id:
        st.error("Avant de commencer à entrer des données, veuillez donner un identifiant à votre notice")


    if projet_id:
        titre_projet = st.text_input("Titre du projet")

        # --- Listes simples (via textarea) ---
        usages_ia = st.multiselect(
            "Usages de l'IA",
            ["Green", "Yellow", "Red", "Blue","white","nice","bug","try","cool","stop","end"],
            accept_new_options=True,
            key=f"{titre_projet}_usages_ia"
        )

        usages_pro = st.multiselect(
            "Usages professionnels (du point de vue du métier du Musée)",
            ["Green", "Yellow", "Red", "Blue","white","nice","bug","try","cool","stop","end"],
            accept_new_options=True,
            key=f"{titre_projet}_usages_pro"
        )

        objet_etude = st.multiselect(
            "Objet d'étude",
            ["Green", "Yellow", "Red", "Blue","white","nice","bug","try","cool","stop","end"],
            accept_new_options=True,
            key=f"{titre_projet}_objet_etude"
        )

        # --- Financement ---
        st.subheader("Financement")
        fourchette = st.selectbox("Fourchette", ["A", "B", "C"])
        financement_exact = st.text_input("Montant exact")

        # --- Dates ---
        st.subheader("Dates du projet")
        nb_dates = st.number_input("Nombre de dates", min_value=1, value=1, step=1)

        dates = []
        for i in range(nb_dates):
            st.markdown(f"**Date {i+1}**")

            col1, col2, col3 = st.columns([1, 1, 3])

            with col1:
                date_value = st.date_input(f"Année / date {1}",value="2020-01-01", key=f"date_{i}", format="DD/MM/YYYY")
            
            with col2:
                type_date = st.selectbox(
                    "Type",
                    ["creation", "jalon", "fin"],
                    key=f"type_{i}"
                )
            
            with col3:
                date_text = st.text_input(
                    "Description",
                    key=f"text_{i}"
                )

            dates.append({
                "id_date": str(i),
                "date": date_value.isoformat() if isinstance(date_value, datetime.date) else None,
                "type": type_date,
                "date_text": date_text
            })

        # --- Statut ---
        st.subheader("Statut du projet")
        statut = st.selectbox("Statut", ["en cours", "terminé"])
        livrable = st.selectbox("Livrables", ["livrables disponibles", "livrables non disponibles"])

        # --- Personnes impliquées ---
        st.subheader("Personnes impliquées")
        nbr_personnes = st.text_area("Personnes impliquées et comment")

        # --- quantités de données ---
        st.subheader("Quantités de données")
        quantite_donnees = st.text_input("Quantités de données du projet")

        # --- Description du projet ---
        st.subheader("Description du projet")
        description = st.text_area("Description du projet")

        ingenierie_interne = st.checkbox("Ingénierie en interne")
        puissance_calcul = st.checkbox("Puissance de calcul en interne")

        source_financement = 0
        livrables = 0
        contacts = 0
        ressources = 0

        # --- Notice ---
        notice_termine = st.checkbox("Notice terminée")

        # --- Construction du JSON ---
        projet_json = {
            "id": projet_id,
            "titre_projet": titre_projet,
            "usages_IA": usages_ia,
            "usage_pro": usages_pro,
            "objet_etude": objet_etude,
            "montant_financement": {
                "fourchette": fourchette,
                "financement_exact": financement_exact
            },
            "dates": dates,
            "statut_projet": {
                "statut": statut,
                "livrable": livrable
            },
            "source_financement": source_financement,
            "nbr_personnes_impliques": nbr_personnes,
            "quantite_donnees": quantite_donnees,
            "puissance_calcul_interne": puissance_calcul,
            "ingenierie_interne": ingenierie_interne,
            "livrables": livrables,
            "ressources": ressources,
            "description": description,
            "contacts": contacts,
            "notice_termine": notice_termine,
        }

        if st.button("Enregistrer la notice"):
            json.dumps()


        st.divider()

        # --- Affichage ---
        st.subheader("JSON généré")
        st.json(projet_json)

        # --- Export ---
        st.download_button(
            "Télécharger le JSON",
            data=json.dumps(projet_json, ensure_ascii=False, indent=4),
            file_name="projet.json"
        )

# Appel de la fonction
add_project()
