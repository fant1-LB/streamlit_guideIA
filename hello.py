import streamlit as st
from pathlib import Path

from modules.data.images import image_path
from modules.entries.add import add_project
from modules.entries.show import afficher_projets

from data.pages.usages_ia.navigation import usage_navigation
from data.pages.accueil import accueil
from data.pages.lexique import lexique
from data.pages.apropos import apropos



def capacites():
    from pathlib import Path
    import streamlit as st
    st.markdown('''Cette section décrit les usages possibles de technologies IA pour améliorer la connaissance scientifique sur les collections. En préambule de cette section, il faut préciser que les technologies IA n'ont pas vocation à remplacer les personnels scientifiques des institutions patrimoniales, ne serait-ce que parce que leur travail est absolument nécessaire pour évaluer et contrôler les systèmes IA. En plus de cela, aucun modèle généraliste n'est à ce jour capable de traiter de manière autonome et vraiment convaincante des collections patrimoniales, et l'entraînement ou _finetuning_ de modèles spécialisés requiert l'aide de spécialistes capables de produire et fournir des données d'entraînement de qualité. L'idée de cette section sera de proposer des outils, algorithmes et applications pour intégrer des éléments IA au travail sur les collections.

Légende des outils : 
- Le drapeau représente le pays ou la zone géographique d'origine du logiciel ou modèle.
- Logiciel en source ouverte ou *open-source* : :unlock: / Logiciel propriétaire : :lock:
- Logiciel gratuit : :free: / Logiciel payant : :moneybag: / Logiciel gratuit avec options payantes : :free:/:moneybag:

                            ''')
    st.set_page_config(layout="wide",)
    tab1, tab2, tab3, tab4 = st.tabs(["Description et classification d'images", "Exploration de grands corpus d'images", "Transcription de textes", "Chatbots et assimilés"])
    with tab1:
        st.markdown("## Description, indexation, classification et segmentation d'images")

                    
        st.markdown("### Principe et intérêt de la segmentation\n\n Un usage fonctionnel de l'IA observé est d'abord la segmentation d'éléments dans des vues numérisées.")
        
        st.markdown('''La segmentation peut servir, sur des corpus sériels, à identifier les éléments représentés sur une image. On peut par exemple faire appel à cette technique pour savoir quels types d'objets sont présents sur des dessins préparatoires, repérer des personnages ou motifs récurrents sur des oeuvres picturales, ou encore repérer des attributs spécifiques sur une oeuvre. Elle peut aussi par exemple servir de pré-traitement pour travailler sur des images contenues dans des ouvrages, ou dans d'autres images. On peut envisager ainsi de repérer les oeuvres dans des photographies d'exposition, dans des catalogues d'exposition, ou encore les illustrations de manuscrits.
                    

Selon les modèles et les besoins, la segmentation peut se contenter d'extraire des formes des images (ce qui peut par exemple accélerer l'annotation manuelle d'images, ou permettre d'identifier les motifs récurrents d'un document à un autre), ou extraire en y associant une identification ou "classe", ce qui permet de savoir directement ce qui, selon le modèle, se trouve sur l'image. Le premier type aura l'avantage de pouvoir fonctionner peu importe le terrain d'étude, là où le second type aura généralement besoin d'être spécialisé avant, ce qui implique un travaille d'annotation pour l'entraînement du modèle.
### Classification et description d'images

Les modèles de classification, eux, vont, comme leur nom l'indique, associer à l'intégralité d'une image une "classe". Contrairement aux modèles de segmentation, qui peuvent, pour certains associer des classes à une partie de l'image, les modèles de classification associent une classe à l'intégralité de l'image. On peut par exemple facilement envisager des traitements qui sépareraient les images en grandes catégories, puis de faire appel à des modèles spécialisés pour affiner le travail sur des corpus déjà triés. Il faut généralement retenir le principe que plus on demandera de classes différentes à un modèle, moins il sera précis pour un entraînement équivalent.
            ''', text_alignment="justify")
        
        st.image(image=image_path("excelsior.jpg"), caption="Extraction par segmentation des photographies d'une page de journal (Excelsior du 24 novembre 1910 - ark:/12148/bpt6k4600008j) à l'aide d'un modèle YOLO")        
                
        st.markdown('''La classification est utile pour catégoriser des images sur des corpus massifs mais relativement homogènes. Comme la segmentation, les modèles de type YOLO ou Dino peuvent réaliser des classifications. On peut également utiliser certains VLM/LLM, comme Florence, ou Qwen pour ces tâches, mais obtenir des sorties structurées et contrôlables de ces modèles demande un travail plus fin. De la même manière que pour la segmentation, un principe général a retenir est que plus il y aura de classes distinctes dans un corpus à classifier, plus il faudra prévoir de données d'entraînement, et plus un modèle sera susceptible de commettre des erreurs.

La description et l'indexation d'images sont deux objets problématiques non résolus au moment d'écriture de ce guide. La description en langage naturel est envisageable avec des modèles type VLM, mais cette approche pose le problème de la mesurabilité des résultats. L'indexation sur plusieurs niveaux à l'aide de thésaurus complexes pose un problème différent, qui est l'inadaptation des modèles d'IA contemporains aux plusieurs niveaux que ces référentiels proposent. On peut envisager un traitement par plusieurs modèles de classification pour imiter les différents niveaux d'un thésaurus, mais il faut noter que la multiplication des traitements multiplie le nombre d'erreurs, et chaque entraînement a un coût en temps humain et en énérgie qui doit être pris en compte. Pour ces deux usages, s'il ne faut pas exclure les traitement entièrement automatisés, sur des quantités raisonnables d'images nous recommanderions plutôt d'avoir recours à l'IA pour appuyer le personnel scientifique, dans le cadre de traitements semi-automatiques. Voir à ce sujet l'onglet consacré à l'exploration de grands corpus d'images.

### Outils et ressources

De nombreux outils et ressources existent à propos de la segmentation et de la classification d'images une sélection non exhaustive ci-dessous :

*   [L'article en profondeur d'IBM consacré aux différents types de segmentation.](https://www.ibm.com/fr-fr/think/topics/image-segmentation)
*   [Roboflow, plateforme en ligne pour la segmentation d'image. La plateforme dispose d'options gratuites et payantes, selon les besoins qu'on a.](https://roboflow.com/) : :us: - :lock: - :free:/:moneybag:
*   [La Google Teachable Machine, application en ligne pour expérimenter avec la classification d'images.](https://teachablemachine.withgoogle.com/train) : :us: - :lock: - :free:
*   [Aikon, plateforme de l'ERC discover à l'Ecole Nationale des Ponts et Chaussées pour la segmentation de manuscrits.](https://aikon-platform.github.io/) : :fr: - :unlock: - :free:
*   [Arkindex, plateforme développée par l'entreprise Teklia, pour le traitement en masse de documents numérisés.](https://www.teklia.com/arkindex) : :fr: - :unlock: - :free:/:moneybag:
*   [Labelstudio, plateforme d'annotation développée par l'entreprise Human Signal pour l'annotation d'images pour différentes formes de segmentation.](https://labelstud.io/) : :us: - :unlock: - :free:/:moneybag:

### Modèles

Si les technologies évoluent très vite, la classification et la segmentation sont dominées par un certain nombre de familles de modèles :

*   [Les modèles Yolo, développés par la société Ultralytics, sont une famille de modèles permettant segmentation, classification, détection de poses, traque d'objets... Ces modèles sont relativement légers et faciles à adapter à des besoins spécifiques.](https://docs.ultralytics.com/fr/) : :us: 
*   [SAM, série de modèles de segmentation développés par Meta, ayant la capacité de segmenter une image sans essayer d'attribuer une classe aux éléments ségmentés. Les versions les plus récentes permettent de segmenter selon un prompt.](https://github.com/facebookresearch/segment-anything) : :us: 
*   [DINO, série de modèles pouvant réaliser des tâches de segmentation variées (segmentation, classification, extraction de zones d'intérêt... etc), développé par Meta.](https://ai.meta.com/research/dinov3/) : :us:
*   [QWEN-VL est la série de modèles de vision par ordinateur issues des LLMs QWEN. Son point fort est la relative facilité avec laquelle il se spécialise.](https://qwen.ai/blog?id=qwen3-vl) : :cn: ''',text_alignment="justify") 
            

    with tab2: 
        usage_navigation()
                
        
    with tab3:
        st.markdown('''Reconnaissance et transcription de textes imprimés et manuscrits
---------------------------------------------------------------- ''')
        st.markdown('''### Principes de la transcription automatique 

Cette section décrira les usages possibles de technologies IA pour transcrire automatiquement du texte dans des documents numérisés. L'OCR (Optical Character Recognition) et l'HTR (Handwritten Text Recognition) sont des technologies qui ont beaucoup évolués ces dernières années grâce aux progrès de l'IA, et en particulier du deep learning. De nombreux outils et applications sont désormais disponibles pour automatiser la reconnaissance de caractères dans des documents imprimés ou manuscrits, avec des niveaux de performance élevés.



Ce sont des technologies plus anciennes et plus éprouvées que la segmentation, ou encore les chatbots présentés dans ce guide. La transcription se sépare en deux grandes catégories : l'OCR et l'HTR. L'OCR se consacre à la reconnaissance de caractères imprimés, l'HTR à la reconnaissance de caractères manuscrits.''', text_alignment = "justify")
        
        st.image(image=image_path("OCR_Hugo_BnF.png"), caption="capture d'écran montrant un résultat d'un OCR sur un texte de Victor Hugo")
        
        st.markdown('''Du fait de la nature très répétitive, et de la relative persistance dans le temps des polices imprimées, les modèles d'OCR sont généralement applicables à un large éventail de documents. L'usage de cette technologie se fait donc plus facilement à partir de solutions pré-existantes, déjà développées dans le cadre de projets de recherche précédents, ou pour le traitement de texte contemporain. Plus que la transcription même, la difficulté va résider dans la structuration des transcriptions si la mise en page du document est complexe. A l'inverse, l'HTR, du fait de la plus grande variabilié des écritures manuscrites, en particulier dans le temps, va généralement demander un travail de spécialisation des modèles, même si les VLMs les plus récents viennent remettre en cause ce paradigme. Dans les deux cas, il faudra prévoir une "vérité terrain", c'est à dire quelques documents représentatifs du corpus traité transcrits à la main, pour mesurer la fiabilité de l'instrument d'OCR ou d'HTR utilisé. La qualité d'une transcription est généralement mesurée à partir du CER (<em>Caracter Error Rate</em>), c'est à dire le pourcentage de caractères faux dans la transcription par rapport à la "vérité terrain", ou le WER (<em>Word Error Rate</em>), qui est de son côté le pourcentage de mots faux.



La mise en place de ces technologies dépendra de vos objectifs, de vos compétences techniques et de vos ressources matérielles. Pour des besoins ponctuels ou des volumes limités, des solutions toutes faites en ligne peuvent être suffisantes. Pour des besoins plus importants ou des exigences spécifiques, la mise en place de chaînes de traitement plus complètes ou personnalisées sera sans doute nécessaire. Comme toujours, il faut évaluer avant de se lancer dans le projet la pertinence du temps et des coûts engagés dans le projet par rapport à un travail manuel.

Il est important de noter que la qualité des résultats dépendra fortement de la qualité des images numérisées et des spécificité des documents (langue, écriture, mise en page...).

Comme pour la plupart des modèles d'IA, il faut prévoir de la puissance de calcul pour l'application sur de larges corpus, et pour l'entraînement ou réentraînement de modèles spécialisés. Pour les moyens humains, une personne qui parle la langue, et est capable de lire l'écriture du document est évidemment indispensable ne serait-ce que pour établir la "vérité terrain". Il ne faut pas attendre de la machine d'être capable de transcrire ce qu'aucun humain ne saurait lire.''', text_alignment ="justify")
        st.image(image=image_path("infographie_difficultes_htr_ocr.JPG"), caption="Exemple de documents et des difficultés posées par leur transcription")

        st.markdown('''### Usages de transcription automatique

A partir des ces technologies, on peut aider à réaliser de très nombreuses tâches en lien avec les collections. Les transcriptions automatiques peuvent servir à la documentation des collections, de leurs parcours et de leurs provenances. La transcription de documents peut grandement faciliter l'accès aux documents concernant les oeuvres. En plus de cela, les VLMs contemporains sont capables de transformer la transcription en données structurées. On peut ainsi envisager des traitements qui permettent par exemple d'extraire de catalogues de ventes, ou de registres divers, des informations ciblées pour documenter un lot d'oeuvres.

En plus de cela le fait de diposer de transcriptions intégrales de textes permet évidemment des recherche beaucoup plus faciles dans des grands lots de textes numérisés, ou encore d'extraire des informations d'objets mêlant texte et image, comme des affiches ou des albums de photographies.

### Outils et ressources

De nombreux outils et ressources existent spécifiquement pour faire de l'OCR et HTR, une sélection non exhaustive ci-dessous :

*   [Transkribus, plateforme pour la numérisation, reconnaissance et transcription de textes historiques.](https://www.transkribus.org/fr) : 🇪🇺  - :lock: - :free:/:moneybag:
*   [E-scriptorim, plateforme pour la transcription de textes de l'INRIA.](https://escriptorium.inria.fr/) : :fr: - :lock: - :free:
*   [HTR united, catalogue de jeux de données pour la transcription automatique.](https://htr-united.github.io/)  
*   [Awesome OCR (2021), guide des bases et des ressources pour l'OCR en 2021.](https://github.com/kba/awesome-ocr)  
*   [Arkindex, plateforme développée par l'entreprise Teklia, pour le traitement en masse de documents numérisés.](https://www.teklia.com/arkindex) : :fr: - :unlock: - :free:/:moneybag:
*   [Calfa Vision, plateforme développée par l'association Calfa, pour la transcriptions d'écritures non latines.](https://vision.calfa.fr/) : :fr: - :lock: - :free:/:moneybag:
*   [La liste des modèles d'OCR disponibles sur hugging face.](https://huggingface.co/models?pipeline_tag=image-to-text)
*   [Kraken OCR, l'un des premiers moteurs d'OCR performants s'étant imposé dans les LAMs français. Il permet d'utiliser et ré-entraîner un certain nombre de modèles ouverts.](https://github.com/mittagessen/kraken) : :fr:/ 🇪🇺  - :unlock: - :free:

### Modèles

Si les technologies évoluent très vite, au moment d'écriture de ce guide nous pouvons citer un certain nombre de modèles IA capables de réaliser des tâches de transcription adaptés au contexte patrimonial.

*   [Pero-OCR, modèle de transcription de revues et journaux.](https://pero-ocr.fit.vutbr.cz/) : :czech_republic:
*   [GLM-OCR, modèle de transcription généraliste.](https://huggingface.co/zai-org/GLM-OCR) : :cn:
*   [Paddle-OCR, modèle de transcription généraliste](https://github.com/PaddlePaddle/PaddleOCR) : :cn:
*   [Mistral OCR, modèle de transcription de Mistral AI. Ce modèle a l'avantage d'être plutôt plus adapté au français qu'une partie de ses concurrents](https://mistral.ai/news/mistral-ocr) : :fr:
*   [Tesseract, modèle historique dominant pour l'OCR, disponible en plus d'une centaine de langages.](https://github.com/tesseract-ocr/tesseract) : :us:
*   [QWEN-VL est la série de modèles de vision par ordinateur issues des LLMs QWEN, utilisables y compris pour des tâches de transcription. Son point fort est la relative facilité avec laquelle il se spécialise.](https://qwen.ai/blog?id=qwen3-vl) : :cn:
                ''', text_alignment ="justify")

            

    
    tab4.markdown(""" 
### Chatbots et interactions en langage naturelle ###             
Les chatbots sont probablement l'application contemporaine du *machine-learning* la plus présente dans l'espace public. 
Il est aujourd'hui possible de spécialiser les LLMs génératifs derrière les chatbots comme ChatGPT, Le Chat (Mistral) ou encore Claude sur des sujets spécifiques de nombreuses manière différentes. Les plus connues sont le RAG, présenté dans notre lexique, mais aussi des choses comme le [LoRa](https://www.ibm.com/think/topics/lora) ou encore les [MCP](https://www.ibm.com/fr-fr/think/topics/model-context-protocol), qui permettent à une IA de consulter une base de données.
                  
Même dans le cadre de modèles spécialisés, à l'inverse d'autres usages présentés dans ce guide, le format de réponses d'un chatbot, en langage naturel, rend l'évaluation de leur fiabilité plus complexe.
En plus de cela, il faut faire attention aux solutions "toutes faites" en la matière qui font souvent appel à des APIs, c'est à dire qui font appel à un service externe pour interroger le modèle. L'appel à une API implique une sortie des données de l'institution dont il faut réflechir au cadre légal et aux implications. L'appel aux APIs est d'autant plus courant pour ce genre de technologies que la puissance de calcul qu'elles requièrent devient plus rapidement élevée que pour d'autres modèles aux fonctionnalités et connaissances plus limitées.
Des technologies de chatbot ont néanmoins montré des potentialités réelles par exemple pour retrouver rapidement des notices liées dans des bases de données ou restituer de manière synthétique des points spécifiques contenus dans des grandes masses d'information. Ils ont également pu être utilisés à des fins de médiation.

### Outils et ressources 
* [NotebookLM, outil integré de google pour interroger des documents à l'aide des modèles Gemini](https://notebooklm.google/) : :us: - :lock: - :free:/:moneybag:    
* [Ollama, outil de déploiement de LLMs en local](https://ollama.com/) : :us: - :unlock: - :free:/:moneybag:

### Exemples de modèles               
* [La série des modèles Mistral, de l'entreprise française Mistral AI. Il en existe de plusieurs tailles et un certain nombre de modèles spécialisés (Mistral OCR, Voxtral...)](https://huggingface.co/mistralai) : :fr:
* [Les modèles Gemma, modèles ouverts de Google, conçus pour fonctionner sans disposer d'une très grande puissance de calcul](https://deepmind.google/models/gemma/) : :us:
* [Les modèles QWEN, modèles ouverts de l'entreprise chinoise Alibaba Cloud.](https://huggingface.co/Qwen) : :cn:                             """)

def projets():
    st.html("to be done")

page_names_to_func = {"Accueil": accueil, 
                      "Capacités de l'IA": capacites,
                      "Projets":afficher_projets,
                      "Lexique": lexique,
                      #"Ajouter un projet":add_project,
                      "À propos": apropos}

demo_name = st.sidebar.selectbox("Sélectionnez la page qui vous intéresse", page_names_to_func.keys(), index=0)
page_names_to_func[demo_name]()
