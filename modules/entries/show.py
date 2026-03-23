import streamlit as st
import json
import os

def charger_donnees_projets(directory="data/projects_entries"):
    """Récupère tous les JSON dans le dossier data/project_entries."""
    projets = []
    if not os.path.exists(directory):
        return projets
    
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                try:
                    projets.append(json.load(f))
                except Exception:
                    continue
    return projets

def afficher_projets():
    # 1. Chargement initial de la base complète
    tous_les_projets = charger_donnees_projets()
    
    if not tous_les_projets:
        st.info("La base de données est vide (aucun JSON trouvé dans data/project_entries).")
        return

    # 2. Zone de recherche
    st.markdown("## 🔍 Recherche & Filtres")
    search_query = st.text_input(
        "Rechercher un mot-clé (nom, date, technologie, finance...)", 
        placeholder="Tapez votre recherche ici...",
        value=""
    ).lower()

    # 3. Logique de filtrage
    # Si la barre est vide, on garde tout. Sinon, on filtre.
    if search_query.strip() == "":
        projets_a_afficher = tous_les_projets
    else:
        projets_a_afficher = [
            p for p in tous_les_projets 
            if search_query in str(p).lower()
        ]

    # Petit indicateur du nombre de résultats
    st.caption(f"Affichage de {len(projets_a_afficher)} projet(s) sur {len(tous_les_projets)}")
    st.divider()

    # 4. Affichage des blocs informatifs
    if not projets_a_afficher:
        st.warning("Aucun projet ne correspond à votre recherche.")
    else:
        for p in projets_a_afficher:
            with st.container(border=True):
                # --- TITRE ET IDENTIFIANTS ---
                st.markdown(f"### {p.get('titre_projet', 'Projet sans titre')}")
                # st.markdown(f"**ID Unique :** `{p.get('id_unique')}` | **ID :** `{p.get('id')}`")
                
                # --- DESCRIPTION ---
                st.write(f"**Description :** {p.get('description')}")

                # --- ÉQUIPE ---
                participants = p.get('participants', [])
                equipe = ", ".join([f"{part.get('name')} ({part.get('type')})" for part in participants])
                st.write(f"**Participants :** {equipe if equipe else 'N/A'}")
                st.write(f"**Nombre de personnes impliquées :** {p.get('nbr_personnes_impliques')}")

                # --- TECHNIQUE ---
                st.write(f"**Méthodes IA :** {', '.join(p.get('methodes_IA', []))}")
                st.write(f"**Objets d'étude :** {', '.join(p.get('objet_etude', []))}")
                st.write(f"**Usage professionnel :** {', '.join(p.get('usage_pro', []))}")
                
                # --- DONNÉES ET INFRA ---
                qte_donnees = " - ".join([str(q) for q in p.get('quantite_donnees').split("\n") if q])
                st.write(f"**Quantité de données :** {qte_donnees}")
                st.write(f"**Puissance de calcul interne :** {'Oui' if p.get('puissance_calcul_interne') else 'Non'}")
                st.write(f"**Ingénierie interne :** {'Oui' if p.get('ingenierie_interne') else 'Non'}")

                # --- HISTORIQUE ---
                st.write("**Historique des dates :**")
                for d in p.get('dates', []):
                    st.write(f"• {d.get('date')} : {d.get('date_text')} ({d.get('type')})")

                # --- FINANCE ---
                financement = p.get('montant_financement', {})
                st.write(f"**Fourchette de financement :** {financement.get('fourchette')}")
                st.write(f"**Sources :** {', '.join(p.get('source_financement', []))}")

                # --- STATUT ET LIVRABLES ---
                statut_info = p.get('statut_projet', {})
                st.write(f"**Statut :** {statut_info.get('statut')} | **Livrable :** {statut_info.get('livrable')}")
                st.write(f"**Types de livrables :** {' - '.join([l for l in p.get('livrables').split("\n") if l])}")

                # --- ÉTAT DE LA FICHE ---
                # st.write(f"**Notice terminée :** {'✅ Oui' if p.get('notice_termine') else '❌ Non'}")