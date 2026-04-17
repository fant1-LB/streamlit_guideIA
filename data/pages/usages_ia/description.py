import streamlit as st
from modules.data.images import image_path

def usage_description_text():
    st.markdown("## Description, indexation, classification et segmentation d'images")

    st.markdown("Les modèles d’intelligence artificielle peuvent être mobilisés pour accomplir différentes tâches liées à la documentation des collections. Leur utilisation suppose toutefois la disponibilité préalable de versions numérisées des images ou des vidéos. Une très haute définition n’est souvent pas indispensable : dans la pratique, la plupart de ces modèles réduisent les dimensions des images lors du traitement afin d’optimiser leurs performances et de limiter les ressources de calcul nécessaires.")

    st.markdown("### Principe et intérêt de la segmentation")

    st.markdown("Un premier usage fonctionnel de l’IA réside dans la segmentation, c’est-à-dire la capacité à identifier, distinguer et isoler différents éléments au sein d’images numérisées.")
    
    st.markdown('''La segmentation peut constituer un outil pour analyser des corpus d’images sérielles en permettant d’identifier précisément les éléments représentés. Elle peut notamment être mobilisée pour repérer des objets, des personnages ou des motifs récurrents au sein d'images, notamment des photographies, des dessins ou d’œuvres picturales. Par ailleurs, elle s’avère  pertinente comme étape de prétraitement pour l’analyse d’images intégrées à des ensembles composites, tels que des ouvrages illustrés, des albums photographiques ou des recueils d’images. Cette approche permet à la fois l’identification automatisée des œuvres, leur extraction de leur contexte d’origine et, par conséquent, facilite leur analyse.''', text_alignment="justify")

    st.markdown('''Un travail d’annotation manuelle est généralement requis avant l’entraînement d’un modèle, afin de lui apprendre à reconnaître des éléments, des motifs et des objets dans une image. Selon les approches et les objectifs, la segmentation peut se limiter à extraire des formes, ce qui peut notamment accélérer l’annotation ou aider à repérer des motifs récurrents d’un document à l’autre. Elle peut aussi aller plus loin en associant à ces formes une étiquette ou une « classe », permettant ainsi d’identifier directement, selon le modèle, ce qui est présent dans l’image. La première approche présente l’avantage d’être adaptable à des contextes variés, tandis que la seconde nécessite en général une spécialisation préalable. Celle-ci repose sur un travail d’annotation plus conséquent, indispensable à l’entraînement du modèle.''', text_alignment="justify")

    st.image(image=image_path("excelsior.jpg"), caption="Extraction par segmentation des photographies d'une page de journal (Excelsior du 24 novembre 1910 - ark:/12148/bpt6k4600008j) à l'aide d'un modèle YOLO")    


    st.markdown("### Classification et description d'images")

    st.markdown('''Les **modèles de classification** attribuent quant à eux une « classe » à une image dans son ensemble. À la différence des modèles de segmentation, qui peuvent associer des catégories à des zones spécifiques, ils produisent une ou plusieurs étiquettes globales pour l'intégralité de l'image. On peut ainsi envisager des traitements consistant à regrouper d’abord les images en grandes catégories, puis à mobiliser des modèles plus spécialisés pour affiner l’analyse sur des corpus préalablement triés. De manière générale, plus le nombre de classes à distinguer est élevé, plus la précision du modèle tend à diminuer à entraînement équivalent.''', text_alignment="justify")
            
    st.markdown('''La classification est particulièrement utile pour organiser de vastes corpus d’images, en particulier lorsqu’ils présentent une certaine homogénéité ou que les catégories à distinguer sont clairement définies. Certains modèles, comme YOLO ou DINO, peuvent être mobilisés pour ce type de tâche, bien qu’ils soient initialement conçus pour la détection d’objets ou l’apprentissage de représentations visuelles. Par ailleurs, des modèles multimodaux (VLM/LLM) tels que Florence ou Qwen permettent également de réaliser des classifications à partir d’instructions en langage naturel. Néanmoins, obtenir des résultats fiables, structurés et facilement exploitables avec ces approches nécessite généralement un travail de paramétrage plus fin. De manière générale, plus le nombre de classes à distinguer est important, plus les besoins en données d’entraînement augmentent. À complexité équivalente, cette augmentation s’accompagne souvent d’une baisse de précision et d’un risque accru d’erreurs, en particulier lorsque les catégories sont visuellement proches ou déséquilibrées.''')

    st.markdown("# Description et indexation des images")

    st.markdown('''La description et l’indexation des images constituent des défis complexes pour l’intelligence artificielle, en particulier dans le contexte des objets patrimoniaux. Ces derniers présentent souvent des caractéristiques rares ou atypiques, et sont peu représentés dans les corpus d’entraînement des modèles généralistes. Si la production de descriptions en langage naturel est aujourd’hui possible grâce à des modèles combinant vision et langage (VLM), elle suppose que ceux-ci aient été exposés à des images suffisamment proches lors de leur entraînement et qu'ils soient capables d’en interpréter correctement les éléments. Par ailleurs, ces traitements demeurent coûteux en ressources de calcul lorsqu’ils sont appliqués à grande échelle. 
    L’intégration de vocabulaires contrôlés représente également une difficulté : les systèmes doivent non seulement en maîtriser la structure, mais aussi en appliquer les règles d’usage de manière cohérente. Plus largement, la mise en œuvre de ces approches automatisées implique un important travail préparatoire (structuration des données, conception de la chaîne de traitement), des compétences techniques en ingénierie, ainsi que des ressources de calcul conséquentes. Elle s’accompagne également, dans la plupart des cas, d’un travail chronophage de vérification et de nettoyage des données produites. 
    Dans ce contexte, plutôt que d'automatiser la chaîne de traitement de la description des images et remplacer les fonctions du personnel scientifique, un travail hybride de description des images mêlé à des outils de compréhension en masse des corpus peut être envisagé, en intégrant des outils d'intelligence artificielle facilitant l'indexation au travail de description des images. (voir à ce sujet l’onglet consacré à l’exploration de grands corpus d’images)''')
                
    st.markdown('''Dans ce contexte, plutôt que de chercher à automatiser entièrement la chaîne de traitement de la description des images, au risque de se substituer aux fonctions du personnel scientifique, il apparaît plus pertinent d’envisager une approche hybride, qui combine le travail de description mené par les experts avec des outils d’analyse à grande échelle des corpus. L’enjeu est plutôt d’intégrer des solutions d’intelligence artificielle conçues pour faciliter et accélérer l’indexation, tout en permettant au personnel scientifique d’intervenir en amont sur la production des données, plutôt que de contrôler les descriptions des images à posteriori en sortie de traitement. (Voir à ce sujet l’onglet consacré à l’exploration de grands corpus d’images.)''')

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