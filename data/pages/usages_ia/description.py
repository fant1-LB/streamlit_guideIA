import streamlit as st
from modules.data.images import image_path

def usage_description_text():
    st.markdown("## Description, indexation, classification et segmentation d'images")

    st.markdown("### Principe et intérêt de la segmentation")

    st.markdown("Un usage fonctionnel de l'IA observé est d'abord la segmentation d'éléments dans des vues numérisées.")
    
    st.markdown('''La segmentation peut servir, sur des corpus sériels, à identifier les éléments représentés sur une image. On peut par exemple faire appel à cette technique pour savoir quels types d'objets sont présents sur des dessins préparatoires, repérer des personnages ou motifs récurrents sur des oeuvres picturales, ou encore repérer des attributs spécifiques sur une oeuvre. Elle peut aussi par exemple servir de pré-traitement pour travailler sur des images contenues dans des ouvrages, ou dans d'autres images. On peut envisager ainsi de repérer les oeuvres dans des photographies d'exposition, dans des catalogues d'exposition, ou encore les illustrations de manuscrits.''', text_alignment="justify")

    st.markdown('''Selon les modèles et les besoins, la segmentation peut se contenter d'extraire des formes des images (ce qui peut par exemple accélerer l'annotation manuelle d'images, ou permettre d'identifier les motifs récurrents d'un document à un autre), ou extraire en y associant une identification ou "classe", ce qui permet de savoir directement ce qui, selon le modèle, se trouve sur l'image. Le premier type aura l'avantage de pouvoir fonctionner peu importe le terrain d'étude, là où le second type aura généralement besoin d'être spécialisé avant, ce qui implique un travaille d'annotation pour l'entraînement du modèle.''', text_alignment="justify")

    st.markdown("### Classification et description d'images")

    st.markdown('''Les modèles de classification, eux, vont, comme leur nom l'indique, associer à l'intégralité d'une image une "classe". Contrairement aux modèles de segmentation, qui peuvent, pour certains associer des classes à une partie de l'image, les modèles de classification associent une classe à l'intégralité de l'image. On peut par exemple facilement envisager des traitements qui sépareraient les images en grandes catégories, puis de faire appel à des modèles spécialisés pour affiner le travail sur des corpus déjà triés. Il faut généralement retenir le principe que plus on demandera de classes différentes à un modèle, moins il sera précis pour un entraînement équivalent.''', text_alignment="justify")
    
    st.image(image=image_path("excelsior.jpg"), caption="Extraction par segmentation des photographies d'une page de journal (Excelsior du 24 novembre 1910 - ark:/12148/bpt6k4600008j) à l'aide d'un modèle YOLO")    
        
    st.markdown('''La classification est utile pour catégoriser des images sur des corpus massifs mais relativement homogènes. Comme la segmentation, les modèles de type YOLO ou Dino peuvent réaliser des classifications. On peut également utiliser certains VLM/LLM, comme Florence, ou Qwen pour ces tâches, mais obtenir des sorties structurées et contrôlables de ces modèles demande un travail plus fin. De la même manière que pour la segmentation, un principe général a retenir est que plus il y aura de classes distinctes dans un corpus à classifier, plus il faudra prévoir de données d'entraînement, et plus un modèle sera susceptible de commettre des erreurs.''')

    st.markdown('''La description et l'indexation d'images sont deux objets problématiques non résolus au moment d'écriture de ce guide. La description en langage naturel est envisageable avec des modèles type VLM, mais cette approche pose le problème de la mesurabilité des résultats. L'indexation sur plusieurs niveaux à l'aide de thésaurus complexes pose un problème différent, qui est l'inadaptation des modèles d'IA contemporains aux plusieurs niveaux que ces référentiels proposent. On peut envisager un traitement par plusieurs modèles de classification pour imiter les différents niveaux d'un thésaurus, mais il faut noter que la multiplication des traitements multiplie le nombre d'erreurs, et chaque entraînement a un coût en temps humain et en énérgie qui doit être pris en compte. Pour ces deux usages, s'il ne faut pas exclure les traitement entièrement automatisés, sur des quantités raisonnables d'images nous recommanderions plutôt d'avoir recours à l'IA pour appuyer le personnel scientifique, dans le cadre de traitements semi-automatiques. Voir à ce sujet l'onglet consacré à l'exploration de grands corpus d'images.''')

    st.markdown("### Outils et ressources")

    st.markdown("De nombreux outils et ressources existent à propos de la segmentation et de la classification d'images une sélection non exhaustive ci-dessous :")

    st.markdown('''
    *   [L'article en profondeur d'IBM consacré aux différents types de segmentation.](https://www.ibm.com/fr-fr/think/topics/image-segmentation)
    *   [Roboflow, plateforme en ligne pour la segmentation d'image. La plateforme dispose d'options gratuites et payantes, selon les besoins qu'on a.](https://roboflow.com/) : :us: - :lock: - :free:/:moneybag:
    *   [La Google Teachable Machine, application en ligne pour expérimenter avec la classification d'images.](https://teachablemachine.withgoogle.com/train) : :us: - :lock: - :free:
    *   [Aikon, plateforme de l'ERC discover à l'Ecole Nationale des Ponts et Chaussées pour la segmentation de manuscrits.](https://aikon-platform.github.io/) : :fr: - :unlock: - :free:
    *   [Arkindex, plateforme développée par l'entreprise Teklia, pour le traitement en masse de documents numérisés.](https://www.teklia.com/arkindex) : :fr: - :unlock: - :free:/:moneybag:
    *   [Labelstudio, plateforme d'annotation développée par l'entreprise Human Signal pour l'annotation d'images pour différentes formes de segmentation.](https://labelstud.io/) : :us: - :unlock: - :free:/:moneybag:
    ''')
    
    st.markdown("### Modèles")

    st.markdown('''Si les technologies évoluent très vite, la classification et la segmentation sont dominées par un certain nombre de familles de modèles :''')
    
    st.markdown('''
    *   [Les modèles Yolo, développés par la société Ultralytics, sont une famille de modèles permettant segmentation, classification, détection de poses, traque d'objets... Ces modèles sont relativement légers et faciles à adapter à des besoins spécifiques.](https://docs.ultralytics.com/fr/) : :us: 
    *   [SAM, série de modèles de segmentation développés par Meta, ayant la capacité de segmenter une image sans essayer d'attribuer une classe aux éléments ségmentés. Les versions les plus récentes permettent de segmenter selon un prompt.](https://github.com/facebookresearch/segment-anything) : :us: 
    *   [DINO, série de modèles pouvant réaliser des tâches de segmentation variées (segmentation, classification, extraction de zones d'intérêt... etc), développé par Meta.](https://ai.meta.com/research/dinov3/) : :us:
    *   [QWEN-VL est la série de modèles de vision par ordinateur issues des LLMs QWEN. Son point fort est la relative facilité avec laquelle il se spécialise.](https://qwen.ai/blog?id=qwen3-vl) : :cn: 
    ''',text_alignment="justify") 