import streamlit as st

from modules.data.images import image_path

def usage_navigation():
    st.markdown("## Les outils d'intelligence artificielle pour l'exploration de grands corpus d'images")
    st.markdown("### Similarité et *clustering*")

    with st.container(
        width="stretch", # "stretch", "content" ou un entier (ex: 500)
        horizontal_alignment="center", 
        gap="small"
    ):
        st.image(image=image_path("pixplot.png"), caption= "Visualisation globale de 11974 peintures italiennes du RETIF (INHA) grâce au logiciel PixPlot", width=800)
        
    st.markdown("Grâce à des algorithmes de similarité et d’analyse d’images, les outils d’intelligence artificielle rendent possible l’exploration de vastes corpus iconographiques dépourvus de métadonnées. Ils présentent un intérêt majeur pour les collections de photographies, d’arts graphiques ou d’objets, en facilitant l’identification de motifs récurrents, la classification des œuvres selon différents critères et la rédaction de descriptions ou leur indexation.")
    st.markdown("Ces outils permettent d’identifier des « clusters » (ou groupes) au sein d’un corpus d’images, c’est-à-dire des ensembles d’images présentant des similarités visuelles ou formelles. Ces regroupements peuvent être établis à partir du contenu iconographique ou de caractéristiques telles que les couleurs, les textures, les formes ou les compositions. Par ailleurs, ces outils se révèlent également utiles pour repérer d’éventuels doublons au sein du corpus.")

    st.markdown("### Rechercher des images plein texte")

    with st.container(
        width="stretch", # "stretch", "content" ou un entier (ex: 500)
        horizontal_alignment="center", 
        gap="small"
    ):
        st.image(
            image=image_path("tennis_panoptic.JPG"), 
            caption="Recherche via l'application Panoptic, et un modèle CLIP, des images associées au mot tennis dans le dataset bbc_news_alltime sur huggingface.",
            width=800
        )
    st.markdown("Certains modèles permettent également d’effectuer des recherches au sein d’images non documentées à l’aide du langage naturel. Entraînés à associer des images à des descriptions textuelles, ils peuvent ensuite être appliqués à de nouveaux corpus iconographiques afin d’en faciliter l’exploration et la description.")

    with st.expander("Quelques technologies et modèles"):
        st.markdown("#### CLIP")
        st.markdown("Développé par OpenAI, CLIP (Contrastive Language–Image Pretraining) est un modèle entraîné sur de vastes ensembles d’images et de textes afin d’apprendre à associer descriptions textuelles et contenus visuels. Il permet notamment la recherche d’images en langage naturel et la classification sans entraînement spécifique sur le corpus étudié.")
        st.link_button("En savoir plus", "https://openai.com/index/clip/")

        st.markdown("#### DINO")
        st.markdown("DINO (Self-Distillation with No Labels), développé par Meta AI, est un modèle d’apprentissage auto-supervisé qui apprend des représentations visuelles sans annotations textuelles. Difficile à manipuler, il est cependant particulièrement performant pour regrouper des images similaires, identifier des motifs récurrents et identifier des points d'attention au sein des images.")
        st.link_button("En savoir plus", "https://ai.meta.com/research/dinov3/")

    st.markdown("### Des logiciels faciliant la visualisation et l'annotation de grands corpus")
    st.markdown("Au cours des dernières années, plusieurs logiciels intégrant ces algorithmes ont été développés dans le cadre de projets universitaires français et étrangers. Certains permettent l’exploration et la visualisation de corpus d’images dans des espaces bidimensionnels ou tridimensionnels (ex: PixPlot). D’autres offrent également des fonctionnalités d’annotation, facilitant ainsi le travail de description, d’analyse et d'indexation des corpus iconographiques.")
    
    with st.expander("Quelques exemples de ces logiciels"):
        st.markdown("#### Pixplot")
        st.markdown("Le principe de ces technologies est de transformer les images en des représentations mathématiques complexes, puis, comme illustré ci-dessus, de restituer lesquels de ces objets mathématiques sont les plus proches les unes des autres dans une représentations 2D, pour permettre aux humains d'observer les proximités entre les images.")
        st.markdown("#### VikusViewer")
        st.markdown("#### Panoptic")

    with st.container(border=True):  
        st.markdown("#### En résumé")

        st.markdown("L'exemple ci dessus, avec le logiciel Panoptic, montre les possibilités qu'offrent concrétement ces technologies. On peut ainsi très rapidement extraire d'une masse d'images non annotées des éléments pour les documenter en masse. On peut également envisager des applications qui suggèrent des mots à associer à une image, ou encore des images proches des autres images d'une catégorie d'indexation. Ces technologies ont la capacité de grandement accélerer le travail de documentation des images.")      