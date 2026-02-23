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
    st.markdown("Ces outils permettent d’identifier des « clusters » (ou groupes) au sein d’un corpus d’images, c’est-à-dire des ensembles d’images présentant des similarités visuelles ou formelles.  Par ailleurs, ces outils se révèlent également utiles pour repérer d’éventuels doublons au sein du corpus. Une fois identifiées les logiques sous jacentes à un cluster (couleurs, textures, composition...), l'annotation de l'intégralité du cluster permet de gagner beaucoup de temps par rapport à une annotation manuelle.")

    st.markdown("### Rechercher des images en langage naturel")

    with st.container(
        width="stretch", # "stretch", "content" ou un entier (ex: 500)
        horizontal_alignment="center", 
        gap="small"
    ):
        st.image(
            image=image_path("tennis_panoptic.JPG"), 
            caption="Recherche via l'application Panoptic, et un modèle CLIP, des images associées au mot tennis dans le dataset bbc_news_alltime, qui contient l'intégralité des miniatures du site web de la BBC, sur huggingface.",
            width=800
        )
    st.markdown("Certains modèles permettent également d’effectuer des recherches au sein d’images non documentées à l’aide du langage naturel. Entraînés à associer des images à des descriptions textuelles, ils peuvent ensuite être appliqués à de nouveaux corpus iconographiques afin d’en faciliter l’exploration et la description.")

    st.markdown('''### Modèles
*   [CLIP, modèle texte et image développé par Open AI.](https://openai.com/index/clip/)
*   [Siglip, modèle texte et image développé par google (sur Arxiv).](https://arxiv.org/abs/2303.15343)
*	[DINO, série de modèles pouvant réaliser des tâches de segmentation variées (segmentation, classification, extraction de zones d'intérêt... etc), développé par Meta. Les *embeddings* créés par le modèle peuvent aussi être utilisés à des fins de comparaison.](https://ai.meta.com/research/dinov3/)
''')
       

    
    st.markdown('''### Outils et ressources

De nombreux outils et ressources existent pour l'exploitation de ces techniques de similarité : 
*   [Panoptic, outil d'annotation et de navigation dans des grands corpus d'images](https://www.transkribus.org/fr)
*   [Pixplot, outil de visualisation de clusters de similarité](https://dhlab.yale.edu/projects/pixplot/)
*   [Le Match-Engine, cette technologie plus ancienne n'est pas issue du machine learning, mais réalise également des tâches de repérage d'images similairesou de doublons](https://reuse.diglib.org/toolkit/tineye-matchengine/)''', text_alignment="justify")

    