import streamlit as st
from pathlib import Path
import streamlit as st

from modules.data.images import image_path
from modules.entries.add import add_project
from modules.entries.show import afficher_projets

from data.pages.usages_ia.navigation import usage_navigation

def accueil():
    st.write("# Bienvenue sur notre guide consacré aux projets IA pour l'étude des collections patrimoniales en France.")
    st.sidebar.success("Naviguez dans le guide.")

    st.html('''<p> Ce guide de ressources a pour objectif de donner un premier aperçu des possibilités de l'intelligence artificielle pour le traitement de collections patrimoniales. Dans le contexte de ce guide le terme IA recouvrira les technologies
                ayant recours au <i> machine-learning</i>. Ce guide ne traitera pas de formes d'IA tel que les forêts de
                décision ou les chaînes de Markov.</p>
             
             <p> Ce guide est destiné à des personnes ayant des niveaux informatiques variables, et est pensé pour n'avoir aucun prérequis technique d'entrée. Si certains termes vous sont étrangers n'hésitez pas à consulter notre lexique.
            Du fait de l'évolution très rapide des technologies dans ce secteur certains des projets et certaines des applications présentées dans ce guide peuvent être obsolètes au moment de la lecture.
            En introduction de ce guide nous voulons également insister sur le fait que l'"IA" ne doit pas être une fin en soi, et devrait être utilisée comme un outil pour accomplir une mission.
            À ce titre, des questions telles que le régime de droit des données traitées, le coût économique, écologique ou l'accompagnement au changement doivent être réflechies de la même manière que pour n'importe quel outil numérique.</p>
            <p> Enfin il ne faut pas penser l'IA comme un outil "magique" qui réglerait des problèmes importants ou automatiserait des processus sans difficulté. Avant d'atteindre le stade ou la technologie pourra significativement faciliter le travail, il faut compter de très nombreuses heures de travail d'annotation, étude des collections et réflexions techniques.</p>
             ''')
    
    st.markdown('''### Ci-dessous une série de ressources externes pour approfondir les concepts présentés dans ce guide : ###   
- [La stratégie du ministère de la culture pour des intelligences artificielles culturelles et responsables](https://www.culture.gouv.fr/thematiques/innovation-numerique/la-strategie-du-ministere-pour-des-intelligences-artificielles-culturelles-et-responsables)
- [AI4LAM, communauté internationale consacrée aux usages de l'intelligence artificielle pour les bibliothèques, archives et musées](https://sites.google.com/view/ai4lam) - [Github de la communauté](https://github.com/AI4LAM)              
- [Guide de planification des projets IA de la Librairie du Congrès Américaine](https://blogs.loc.gov/thesignal/2023/11/introducing-the-lc-labs-artificial-intelligence-planning-framework/)
- [Blog de Pictoria - Consortium HN consacré à l'usage de l'intelligence artificielle pour les images en Sciences Humaines et Sociales](https://pictoria.hypotheses.org/)
- [Résultats du programme The Museums + AI, expérimentation autour de l'IA, l'éthique et les musées (2019-2020)](https://themuseumsai.network/)
- [L'intelligence artificielle à la Bibliothèque Nationale de France, ressources, cadres d'usages, projets...](https://www.bnf.fr/fr/lintelligence-artificielle-la-bnf)
- [Guide complet d'IBM consacré au _machine learning_ ou apprentissage machine](https://www.ibm.com/think/machine-learning#605511093)
- [Google ML glossary, dictionnaire de google pour le _machine learning_ ou apprentissage machine](https://developers.google.com/machine-learning/glossary?hl=en)
                ''')

    

def lexique ():
    st.html('''<h3 id="API">API</h3>
            <p>Une API, pour <i>application programming interface</i> ou « interface de programmation d'application »
                est un système qui permet de connecter un logiciel à une machine en ligne. Les APIs permettent par exemple d'envoyer sur un serveur extérieur des
                requêtes à des modèles d'IA trop lourds pour fonctionner sur un ordinateur ou serveur de l'institution.
                Un traitement qui implique de faire appel à une API implique donc l'accès par un acteur extérieur à l'institution aux documents traités, et donc une vigilance particulière quant au régime de droit des documents en question.
                La plupart des grands <i>Large language models</i> commerciaux peuvent être utilisés via leur API. </p>
            <h3 id="Annotations">Annotations</h3>
            <p>Dans un contexte IA, les annotations sont les données que l’on va utiliser pour entraîner ou réentrainer
                un modèle. La forme de l’annotation dépend du modèle que l’on veut entraîner ou réentrainer. La
                transcription d’une zone de texte est une annotation dans un contexte d’OCR/HTR. Un “tag” associé à
                l’image est une annotation pour un modèle de classification. Une zone délimitée sur une image est une
                annotation pour un modèle de segmentation. Obtenir des annotations de qualité est un enjeu primordial
                dans n’importe quel projet IA.</p>
            <h3 id="chatbot">ChatBot ou agent conversationnel</h3>
            <p>Un chatbot est un logiciel conçu pour interagir avec un utilisateur au travers d’échanges textuels ou
                vocaux. Cette technologie préexiste aux LLMs et à l’émergence de l’IA mais a passé un cap en étant
                associés à des LLMs. Grâce à eux le chatbot peut converser avec l’utilisateur dans un langage naturel.
                C’est probablement l’application de l’IA la plus connue du grand public. Un chatbot IA est souvent nommé
                d’après le modèle qui le fait fonctionner.<br>
                Ex : ChatGPT, Le Chat (Mistral), Claude, Gemini…</p>
            <h3 id="computerVision">Computer vision</h3>
            <p>La <em>Computer Vision</em> ou vision par ordinateur en français, sont l’ensemble des technologies
                permettant l’interprétation d’images par une machine. L’OCR, l’HTR, la segmentation d’images ou encore
                la détection d’objets sont des applications possibles de <em>Computer Vision</em>.</p>
            <h3 id="Entraînementréentrainement">Entraînement/réentrainement</h3>
            <p>L’entraînement est le moment où l’on commence à alimenter en données un algorithme ou modèle pour qu’il
                se modifie jusqu’à atteindre les résultats qu’on désire. Un entraînement peut se faire à partir
                de données spécifiquement annotées par un humain (approche supervisée) ou brutes (approche
                non supervisée). Cette étape demande une puissance de calcul
                considérable. Le réentraînement est le fait de faire subir un nouvel entraînement à un modèle existant
                pour le modifier et l’adapter à des besoins spécifiques.</p>
            <h3 id="Finetuning">Finetuning</h3>
            <p>Le <em>finetuning</em> est l’ensemble des manipulations que l’on fait sur un modèle pour améliorer ses
                résultats. Le <em>finetuning</em> peut passer par la modification de paramètres, d’un <em>prompt</em>,
                ou encore par un réentraînement.</p>
            <h3 id="GPU">GPU</h3>
            <p>Un GPU, ou <em>Graphic Processing Unit</em> est une unité de calcul assurant les fonctions de traitement des
                d’images. Le GPU est le coeur de ce qu’on appelle plus couramment les cartes
                graphiques. Originellement les GPUs ont été développés pour les jeux vidéos et le calcul de trajectoires. Avec l’émergence de l’IA, la communauté scientifique s’est rendue compte qu’ils
                étaient bien plus efficaces pour le calcul des objets mathématiques (vecteurs) qu’utilisent la plupart des modèles d’IA que les
                CPUs (ou processeurs) traditionnels de nos ordinateurs. L’utilisation de GPUs accélère grandement le
                traitement par IA de données. Avoir un GPU est même nécessaire pour les modèles les plus lourds et les
                entraînements et réentraînements. </p>
            <h3 id="LLM">LLM</h3>
            <p>Un LLM, ou grand modèle de langue, est un modèle IA capable d'interpréter et génerer du langage naturel.<br>
                Un modèle de langue est un modèle probabiliste basé sur la distribution d’éléments linguistiques (lettres,
                phonèmes, mots) dans une langue naturelle. Les plus connus sont des modèles génératifs qui calculent le
                mot suivant ou la lettre suivante le plus probablent dans une séquence de mots, selon un contexte, pour interagir avec
                l’utilisateur. Un grand modèle de langue se différencie d'un modèle de langue classique par la masse de son corpus d'entraînement et des ses paramètres, l'unité utilisée pour mesurer la taille d'un modèle d'IA.Certains LLMs sont également capables de traiter des images, on les appelle alors aussi
                des VLM (<i>vision-language model</i>).<br>
                Ex : GPT-4, DeepSeek-R1, Llama-3 …</p>
            <h3 id="Modèle-IA">Modèle IA</h3>
            <p>Un modèle IA est un algorithme capable (avec plus ou moins d’efficacité) d’effectuer un ensemble de
                tâches pour lesquelles on l’a entraîné. Il reçoit un type de données en entrée, et en propose un autre
                en sortie. Le terme “modèle” s’applique en IA peu importe le domaine. On appelle un modèle qui peut
                recevoir plusieurs types de données en entrée (par exemple texte ET image) un modèle
                <em>multimodal</em>. On distingue aussi généralement les modèles <em>spécialisés</em>, capables de
                réaliser une unique tâche (par exemple détecter les visages sur une image), des modèles
                <em>généralistes</em>, ou <em>modèles de fondation</em> capables de réaliser des tâches ou de traiter des données très variées (comme la plupart des LLMs génératifs grand public). Les
                modèles spécialisés requièrent habituellement moins de puissance de calcul que les généralistes.
            </p>
            <p>Ex : un modèle YoloV8n reçoit une image en entrée, et propose les coordonnées et le nom d’objets détectés sur
                l’image en sortie. Tesseract-ocr reçoit une image de texte imprimé et propose une transcription en
                sortie.</p>
            <h3 id="OCRHTR">OCR/HTR</h3>
            <p>OCR (pour <em>Optical Caracter Recognition</em>) et HTR (pour <em>Handwritten Text Recognition</em>)
                sont les noms données à la transcription automatique de texte imprimé (pour l’OCR) et manuscrit (pour
                l’HTR). Ces deux technologies peuvent être rassemblées sous le terme d'"ATR", pour <em> Automatic Text Recognition </em> <br>
                Ex : Tesseract-ocr, pero-ocr, monkey-ocr…</p>
            <h3 id ="Plongement">Plongement </h3>
            Un plongement, ou <em> embedding </em> est un objet mathématique complexe, créé et interprété par un modèle pour manipuler les données qu'on lui donne à traiter.
            <h3 id="Post-correction">Post-correction</h3>
            <p>La post-correction est le travail que l’on fait après l’application d’un modèle IA pour corriger les
                erreurs qu’il commet. Selon les situations la post-correction sera nécessaire ou non. Selon les
                situations elle peut également être automatisée.</p>
            <p> Par exemple, la post correction d'une transcription peut être une relecture humaine pour vérifier l'absence de mots inventés. 
            <h3 id="RAG">RAG</h3>
            <p>Le RAG (ou Retrieval Augmented Generation) est une méthode permettant de donner de grosses quantités
                d’informations à une IA type LLM. Pour cela l’utilisateur va donner accès à son LLM à des sources d'information externes (base de donnée, moteur de recherche...). Cette
                technique permet notamment de doter des LLMs de connaissances plus précises dans un domaine particulier.
            </p>
            <h3 id="VLM">VLM</h3>
            <p>Un VLM (ou <em>Vision Language Model</em>) est un modèle IA proche du LLM, mais capable de traiter simultanément du texte et des 
            images. Contrairement aux modèles de vision par ordinateur traditionnels qui se 
            limitent à classifier ou détecter des objets, les VLM peuvent raisonner sur le contenu visuel et répondre à des questions 
            ouvertes en langage naturel. Ces modèles permettent la description d'images, la compréhension de documents structurés ou la recherche sémantique avancée dans des images.
            </p>''')





def capacites():
    from pathlib import Path
    import streamlit as st
    st.markdown('''Cette section décrira les usages possibles de technologies IA pour améliorer la connaissance scientifique sur les collections. En préambule de cette section, il faut préciser que les technologies IA n'ont pas vocation à remplacer les personnels scientifiques des institutions patrimoniales, ne serait-ce que parce que leur travail est absolument nécessaire pour évaluer et contrôler les systèmes IA. En plus de cela, aucun modèle généraliste n'est à ce jour capable de traiter de manière autonome et vraiment convaincante des collections patrimoniales, et l'entraînement ou _finetuning_ de modèles spécialisés requiert l'aide de spécialistes capables de produire et fournir des données d'entraînement de qualité. L'idée de cette section sera de proposer des outils, algorithmes et applications pour intégrer des éléments IA au travail sur les collections.
''')
    st.set_page_config(layout="wide",)
    tab1, tab2, tab3, tab4 = st.tabs(["Description et classification d'images", "Exploration de grands corpus d'images", "Transcription de textes", "Chatbots et assimilés"])
    with tab1:
        st.markdown('''### Description, indexation, classification et segmentation d'images

                
Un usage fonctionnel de l'IA observé est d'abord la segmentation d'éléments dans des vues numérisées.''', text_alignment="justify")
        
        st.markdown('''La segmentation peut servir, sur des corpus sériels, à identifier les éléments représentés sur une image. On peut par exemple faire appel à cette technique pour savoir quels types d'objets sont présents sur des dessins préparatoires, repérer des personnages ou motifs récurrents sur des oeuvres picturales, ou encore repérer des attributs spécifiques sur une oeuvre. Elle peut aussi par exemple servir de pré-traitement pour travailler sur des images contenues dans des ouvrages, ou dans d'autres images. On peut envisager ainsi de repérer les oeuvres dans des photographies d'exposition, dans des catalogues d'exposition, ou encore les illustrations de manuscrits.

Selon les modèles et les besoins, la segmentation peut se contenter d'extraire des formes des images (ce qui peut par exemple accélerer l'annotation manuelle d'images, ou permettre d'identifier les motifs récurrents d'un document à un autre), ou extraire en y associant une identification ou "classe", ce qui permet de savoir directement ce qui, selon le modèle, se trouve sur l'image. Le premier type aura l'avantage de pouvoir fonctionner peu importe le terrain d'étude, là où le second type aura généralement besoin d'être spécialisé avant, ce qui implique un travaille d'annotation pour l'entraînement du modèle.

Les modèles de classification, eux, vont, comme leur nom l'indique, associer à l'intégralité d'une image une "classe". Contrairement aux modèles de segmentation, qui peuvent, pour certains associer des classes à une partie de l'image, les modèles de classification associent une classe à l'intégralité de l'image. On peut par exemple facilement envisager des traitements qui sépareraient les images en grandes catégories, puis de faire appel à des modèles spécialisés pour affiner le travail sur des corpus déjà triés. Il faut généralement retenir le principe que plus on demandera de classes différentes à un modèle, moins il sera précis pour un entraînement équivalent.
            ''', text_alignment="justify")
        
        st.image(image=image_path("excelsior.jpg"), caption="Extraction par segmentation des photographies d'une page de journal (Excelsior du 24 novembre 1910 - ark:/12148/bpt6k4600008j) à l'aide d'un modèle YOLO")        
                
        st.markdown('''La classification est utile pour catégoriser des images sur des corpus massifs mais relativement homogènes. Comme la segmentation, les modèles de type YOLO ou Dino peuvent réaliser des classifications. On peut également utiliser certains VLM/LLM, comme Florence, ou Qwen pour ces tâches, mais obtenir des sorties structurées et contrôlables de ces modèles demande un travail plus fin.

La description et l'indexation d'images sont deux objets problématiques loin d'être résolus au moment d'écriture de ce guide. La description est envisageable avec des modèles type VLM, mais pose le problème fondamental de la mesurabilité des résultats. L'indexation sur plusieurs niveaux à l'aide de thésaurus complexes comme le thésaurus Garnier ou IconClass pose un problème différent, qui est l'inadaptation des modèles d'IA contemporains à leurs plusieurs niveaux d'indexation. On peut envisager un traitement par plusieurs modèles de classification pour imiter les différents niveaux d'un thésaurus, mais il faut noter que la multiplication des traitements multiplie le nombre d'erreurs, et chaque entraînement a un coût technique et écologique qui doit être pris en compte. Pour ces deux usages, s'il ne faut pas exclure les traitement entièrement automatisés, sur des quantités raisonnables d'images nous recommanderions plutôt d'avoir recours à l'IA pour appuyer le personnel scientifique, dans le cadre de traitements semi-automatiques.

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
----------------------------------------------------------------

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

### Outils et ressource

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
*   [QWEN-VL est la série de modèles de vision par ordinateur issues des LLMs QWEN. Son point fort est la relative facilité avec laquelle il se spécialise.](https://qwen.ai/blog?id=qwen3-vl) : :cn:
                ''', text_alignment ="justify")

            

    
    tab4.html("""<body> à voir </body>""")

def projets():
    st.html("to be done")

def apropos():
    st.html('''
        <h3>À propos de nous</h3>
        <p>Les auteurs du guide sont trois anciens étudiants du master TNAH de l'école nationale des chartes (promotion 2025) qui ont eu l'idée de ce guide pendant leur stage au sein du Consortium Huma-num PictorIA.
        Ils étaients tous trois dans des institutions patrimoniales ou de recherches différentes (l'INHA, la MSH Mondes et le musée des Arts décoratifs) et se sont retrouvés confrontés aux mêmes problèmes
        et aux mêmes questionnements quant à l'introduction de l'IA dans le cadre du traitement des collections. De là provient l'idée d'un guide qui vulgarise et répertorie les usages, possibilités et précautions
        à considérer lorsqu'on veut utiliser l'IA pour l'analyse d'œuvres culturelles, afin de permettre aux institutions détentrices de collections de mieux s'y retrouver dans la galaxie de projets et de possibilitées
        ouvertes par l'IA. Les auteurs exercent actuellement des fonctions d'ingénieurs d'études à l'École française de Rome, à la MSH Mondes, et au musée des Arts décoratifs où ils continuent de s'impliquer dans des projets de traitement des collections.</p>
    ''')

page_names_to_func = {"Accueil": accueil, 
                      "Capacités de l'IA": capacites,
                      "Lexique": lexique,
                      "Ajouter un projet":add_project,
                      "Projets":afficher_projets,
                      "À propos de nous": apropos}

demo_name = st.sidebar.selectbox("Sélectionnez la page qui vous intéresse", page_names_to_func.keys(), index=0)
page_names_to_func[demo_name]()
