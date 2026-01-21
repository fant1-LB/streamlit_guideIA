import streamlit as st

def accueil():
    import streamlit as st
    st.write("# Bienvenue sur notre guide consacré aux projets IA pour l'études des collections patrimoniales en France.")
    st.sidebar.success("Naviguez dans le guide.")

    st.html ('''<p> Ce guide de ressources a pour objectif de donner un premier aperçu et quelques conseils de bonnes pratiques, en
                particulier issues des expériences du consortium PictorIA sur la manière de traiter des données
                patrimoniales à l'aide d'outils IA. Dans le contexte de ce guide le terme IA recouvrira les technologies
                ayant recours au <i> machine-learning</i>. Ce guide ne traitera pas de formes d'IA tel que les forêts de
                décision ou les chaînes de Markov.</p>
             
             <p> Ce guide est destiné à des personnes ayant des niveaux informatiques variables, et est pensé pour n'avoir aucun prérequis technique d'entrée, si certains termes vous sont étrangers n'hésitez pas à consulter notre lexique.
            Du fait de l'évolution très rapide des technologies dans ce secteur certains des projets et certaines des applications présentées dans ce guide peuvent être obsolètes au moment de la lecture.
            En introduction de ce guide nous voulons également insister sur le fait que l'"IA" ne doit pas être une fin en soi, et devrait être utilisée comme un outil pour accomplir une mission.
            A ce titre, des questions telles que le régime de droit des données traitées, le coût économique, écologique ou l'accompagnement au changement doivent être réflechies de la même manière que pour n'importe quel outil numérique.</p>
             ''')

def lexique ():
    import streamlit as st
    st.html ('''<h3 id="API">API</h3>
            <p>Une API, pour <i>application programming interface</i> ou « interface de programmation d'application »
                est un interface qui permet de connecter un logiciel à une machine en ligne
                pour y effectuer des requêtes. Les APIs permettent par exemple d'envoyer sur un serveur extérieur des
                requêtes à des modèles d'IA trop lourds pour tourner sur notre propre machine.
                Un code, même executé localement, qui implique un appel d'API, partagera des données avec un serveur
                extérieur.
                La plupart des grands <i>Large language models</i> commerciaux peuvent être requêtés via leur API. </p>
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
                d’informations fournies par un humain (approche supervisée) ou sans intervention extérieure (approche
                non supervisée). Cette étape demande une puissance de calcul (et donc une quantité de GPUs)
                considérable. Le réentraînement est le fait de faire subir un nouvel entraînement à un modèle existant
                pour le modifier et l’adapter à nos besoins spécifiques.</p>
            <h3 id="Finetuning">Finetuning</h3>
            <p>Le <em>finetuning</em> est l’ensemble des manipulations que l’on fait sur un modèle pour améliorer ses
                résultats. Le <em>finetuning</em> peut passer par la modification de paramètres, d’un <em>prompt</em>,
                ou encore par un réentraînement.</p>
            <h3 id="GPU">GPU</h3>
            <p>Un GPU, ou <em>Graphic Processing Unit</em> est une unité de calcul assurant les fonctions de calcul
                d’image. Originellement les GPUs ont été développés pour les jeux vidéos et le calcul de déplacements en
                2 ou 3 dimensions. Avec l’émergence de l’IA, la communauté scientifique s’est rendue compte qu’ils
                étaient bien plus efficaces pour le calcul des vecteurs qu’utilisent la plupart des modèles d’IA que les
                CPUs (ou processeurs) traditionnels de nos ordinateurs. L’utilisation de GPUs accélère grandement le
                traitement par IA de données. Avoir un GPU est même nécessaire pour les modèles les plus lourds et les
                entraînements/réentraînements. Le GPU est le coeur de ce qu’on appelle plus couramment les cartes
                graphiques.</p>
            <h3 id="LLM">LLM</h3>
            <p>Un LLM, ou grand modèle de langue, est un modèle IA possédant un grand nombre de paramètres et capable de
                communiquer en langage naturel. Il est entraîné sur des grandes quantités de texte.<br>
                Un modèle de langue est un modèle probabiliste de la distribution d’éléments linguistiques (lettres,
                phonèmes, mots) dans une langue naturelle. Les plus connus sont des modèles génératifs qui calculent le
                mot suivant ou la lettre suivante dans une séquence de mots, selon un contexte, pour interagir avec
                l’utilisateur. Certains LLMs sont également capables de traiter des images, on les appelle alors aussi
                des VLM (<i>vision-language model</i>).<br>
                Ex : GPT-4, DeepSeek-R1, Llama-3 …</p>
            <h3 id="Modèle-IA">Modèle IA</h3>
            <p>Un modèle IA est un algorithme capable (avec plus ou moins d’efficacité) d’effectuer un ensemble de
                tâches pour lesquelles on l’a entraîné. Il reçoit un type de données en entrée, et en propose un autre
                en sortie. Le terme “modèle” s’applique en IA peu importe le domaine. On appelle un modèle qui peut
                recevoir plusieurs types de données en entrée (par exemple texte ET image), un modèle
                <em>multimodal</em>. On distingue aussi généralement les modèles <em>spécialisés</em>, capables de
                réaliser une unique tâche (par exemple détecter les visages sur une image), des modèles
                <em>généralistes</em>, ou <em>modèles de fondation</em> capables de réaliser des tâches ou de traiter des données très variées (comme la plupart des LLMs génératifs grand public). Les
                modèles spécialisés requièrent habituellement moins de puissance de calcul que les généralistes.
            </p>
            <p>Ex : YoloV8 reçoit une image en entrée, et propose les coordonnées et le nom d’objets détectés sur
                l’image en sortie. Tesseract-ocr reçoit une image de texte imprimé et propose une transcription en
                sortie.</p>
            <h3 id="OCRHTR">OCR/HTR</h3>
            <p>OCR (pour <em>Optical Caracter Recognition</em>) et HTR (pour <em>Handwritten Caracter Recognition</em>)
                sont les noms données à la transcription automatique de texte imprimé (pour l’OCR) et manuscrit (pour
                l’HTR). L’OCR est une technologie ancienne qui a émergé dès les années 1960 pour des tâches comme le tri
                du courrier.<br>
                Ex : Tesseract-ocr, pero-ocr, monkey-ocr…</p>
            <h3 id="Post-correction">Post-correction</h3>
            <p>La post-correction est le travail que l’on fait après l’application d’un modèle d’IA pour rattraper les
                erreurs qu’il commet. Selon les situations la post-correction sera nécessaire ou non. Selon les
                situations elle peut également être automatisée par IA.</p>
            <h3 id="RAG">RAG</h3>
            <p>Le RAG (ou Retrieval Augmented Generation) est une méthode permettant de donner de grosses quantités
                d’informations à une IA type LLM. Pour cela l’utilisateur va transformer en une base de vecteurs
                abstraits les données qu’il ou elle veut fournir à son IA, ce qui permettra à l’IA de prendre en compte
                une plus grande quantité d’informations que si elles étaient fournies en langage naturel. Cette
                technique permet notamment de doter des LLMs de connaissances plus précises dans un domaine particulier.
            </p>''')
    
def usages():
    from pathlib import Path
    import streamlit as st
    from utils.functions import image_path
    tab1, tab2, tab3, tab4 = st.tabs(["Description et classification d'images", "Navigation sans métadonnées dans des corpus massifs", "Transcription de textes", "Chatbots et assimilés"])
    liste_images = [i for i in Path('images').iterdir()]
    with tab1:
        st.html('''    <section class="main">
            <h2>1 - Description, indexation, classification et segmentation d'images</h2>
            <p>Cette section décrira les usages possibles de technologies IA pour améliorer la connaissance scientifique
                sur les collections. En préambule de cette section, il faut préciser que les technologies IA actuelles,
                et dans un futur proche n'ont absolument pas vocation à remplacer les personnels scientifiques des
                musées, ne serait-ce que parce que leur travail est absolument nécessaire pour entraîner, évaluer et
                contrôler les systèmes IA.
                En plus de cela, aucun modèle généraliste n'est à ce jour capable de traiter de manière autonome et vraiment convaincante des collections patrimoniales, et l'entraînement ou <i>finetuning </i> de modèles spécialisés
                requiert l'aide de spécialistes
                capables de produire et fournir des données d'entraînement de qualité. L'idée de cette section sera de proposer des
                outils, algorithmes et applications pour intégrer des éléments IA au travail sur les collections.</p>
            <p>Cette section s'appuiera principalement sur les travaux menés dans le cadre des projets Torne-H, Hikaria,
            VHS, Eida</a>, et des laboratoires d'archéologie AOrOc (UMR 8546) et Arscan (UMR 7041).
            </p>
            <p>Un usage efficace à mettre en place de l'IA observé dans ces travaux est d'abord la segmentation
                d'éléments dans des vues numérisées. Ci-dessous un exemple réalisé à l'aide d'un modèle Yolo : </p>''')
        st.image(image="https://cdn.prod.website-files.com/680a070c3b99253410dd3df5/684d85646cdaf7e5252b8497_67ed519cbf3f228c7bb790d7_67c99ff6c72a1cf68c554ff4_Segmentation_fig5.webp", caption="Des engins de chantiers segmentés à l'aide d'un modèle yolo")        
          

        st.html('''<p>La segmentation peut servir, sur des corpus sériels, à identifier les éléments représentés sur une
                images. Dans le cadre du projet Torne-H, un modèle de segmentation a par exemple été entraîné afin de
                déterminer quels types de meubles sont présents sur les dessins préparatoires de designers.
                Elle peut aussi par exemple servir de pré-traitement pour travailler sur des images contenues dans des
                ouvrages, ou dans d'autres images. On peut envisager ainsi de repérer les oeuvres dans des photographies
                d'exposition, dans des catalogues d'exposition, ou encore des manuscrits, comme ça a été le cas pour les
                projets EIDA et VHS. </p>
            <p> Les principales familles de modèles de segmentation sont les modèles comme YOLO, ou DINO, qui associent une
                "classe" à des parties de l'image, ou les modèles SAM, capables de découper les images en fonction des
                traits et de caractéristiques visuelles.</p>

            <p>Les modèles de classification vont, comme leur nom l'indique, associer une image à une "classe".
                Contrairement aux modèles de segmentation, qui peuvent, pour certains associer des classes à une partie
                de l'image, les modèles de classification associent une classe à l'intégralité de l'image.
                Ce type de modèle sera particulièrement intéressant sur un nombre limité de classe. On peut par exemple
                facilement envisager des traitements qui sépareraient les images sur un niveau de description "bas",
                comme c'est le cas dans l'image ci-dessous, ou à l'aide de modèles spécialisés sur des corpus déjà
                triés. C'est par exemple ce qui a pu être fait sur des motifs de tessons de poterie.
                Il faut plus généralement retenir le principe que plus on demandera de classes différentes à un modèle,
                moins il sera précis pour un entraînement équivalent.</p>
            <figure>''')
        
        
        st.image( image= image_path(liste_images, "classification3.png") , caption ="Représentation d'un modèle entraîné par Pierre Husson au service numérique de la recherche de l'INHA. Le modèle détermine si le tableau est un portrait, une nature morte, un paysage, les autres tableaux sont rassemblés sous le titre fourre-tout de 'scène'." )
                
                
        st.html('''<p> La classification est utile pour catégoriser des images sur des corpus massifs mais relativement
                homogènes. En l'état ces modèles ne sont pas fiables sur un trop grand nombre de classes, mais
                fonctionnels sur un petit nombre. Comme la segmentation, les modèles de types Yolo ou Dino peuvent
                réaliser des classifications. On peut également utiliser certains modèles de VLM/LLM, comme Florence, ou Qwen pour ces tâches, mais obtenir
                des
                sorties structurées et controlables de ces modèles demande un travail plus fin. </p>
            <p>La description et l'indexation d'images sont deux objets problématiques loin d'être résolus au moment
                d'écriture de ce guide. La description est envisageable avec des modèles type VLM, mais pose le problème
                fondamental de la mesurabilité des résultats. L'indexation sur plusieurs niveaux à l'aide de thésaurus
                complexes comme le thésaurus Garnier pose un problème différent, qui est l'inadaptation des modèles d'IA
                contemporrains à ces plusieurs niveaux d'indexation.
                On peut envisager un traitement par plusieurs modèles de classification pour imiter les différents
                niveaux d'un thésaurus, mais il faut noter que la multiplication des traitements multiplie le nombre
                d'erreurs, et chaque entraînement a un cout technique et écologique qui doit être pris en compte. Pour
                ces deux usages, s'il ne faut pas exclure les traitement entièrement automatisés, sur des quantités
                raisonnables d'images nous recommanderions plutôt d'avoir recours à l'IA pour appuyer le personnel
                scientifique, dans le cadre de traitements semi automatiques.
            </p>''')

    with tab2: 
        st.html('''
                <h2 id="Début-du-guide">Les outils d'intelligence artificielle pour l'exploration de corpus</h2>
                <p>Les outils d’intelligence artificielle peuvent permettre l’exploration de vastes corpus d’images. Ils
                    présentent un intérêt majeur pour les collections de photographies, d’arts graphiques ou d’objets, en
                    aidant à identifier des motifs similaires, à classer les œuvres selon différentes catégories et à
                    décrire ou indexer les images plus efficacement.</p>
                <p>Au cours des dernières années, dans le cadre de projets de recherche menés par des universités et des
                    établissements publics, en France comme à l’étranger, de nombreuses institutions ont développé des
                    logiciels dédiés à l’exploration et à la navigation au sein de très larges corpus d’images. Ces outils
                    s’appuient sur les progrès récents en vision par ordinateur et en algorithmes de similarité, permettant
                    notamment de regrouper les images d’un même corpus en fonction de leur contenu visuel ou de
                    caractéristiques formelles (couleurs, textures, compositions, etc.).
                </p>
                <p>
                    À condition de disposer d’un nombre suffisant d’images à étudier, les chercheur.euses et les
                    institutions peuvent installer et utiliser aisément plusieurs logiciels gratuits et open source
                    présentés ci-dessous : PixPlot, VIKUS Viewer, Panoptic.
                </p>

                <h3>De nouvelles manières de visualiser de vastes corpus d’images</h3>

                <p>
                    L’utilisation de logiciels comme PixPlot et VIKUS Viewer ouvre de nouvelles perspectives pour
                    l’exploration et la compréhension de vastes corpus d’images.
                </p>''')
        
        st.image(image=image_path(liste_images, "pixplot.png"), caption= "Visualisation globale de 11974 peintures italiennes du RETIF (INHA) grâce au logiciel PixPlot")
        st.html('''<p>PixPlot est un logiciel open source, développé en 2017 par le Yale Digital Humanities Lab de
                    l’université de Yale, dans le prolongement des travaux menés lors du projet Replica. Grâce à des
                    algorithmes d’analyse des images, il permet de visualiser et d’explorer un corpus iconographique en
                    disposant les images dans un espace en deux dimensions en fonction de leurs similarités visuelles.
                </p>''')
        st.image(image=image_path(liste_images, "VikusViewer.png"), caption="Visualisation de 986 dessins et peintures de Vincent van Gogh (1853–90) provenant du Van Gogh Museum à Amsterdam dans VIKUS Viewer")
                
        st.html('''        <p>
                    Le logiciel VIKUS Viewer, développé par l’université de Potsdam, peut organiser les
                    images dans un espace bidimensionnel selon des métadonnées écrites en dure, ou comme Pixplot, selon leur similarité visuelle. Son interface claire et soignée
                    permet également de classer les images selon leur date de création, facilitant une lecture diachronique
                    des corpus.
                </p>

                <h3>
                    Faciliter l’annotation et la documentation des images
                </h3>''')

        st.image(image=image_path(liste_images, "panoptic.png"), caption='Interface de Panoptic')      
                    
                  

        st.html('''        <p>
                    Le logiciel Panoptic, développé par le CERES, est dédié à la visualisation et à l’annotation de grands
                    corpus d’images. Il s’appuie sur différents algorithmes de similarité visuelle que l’utilisateur peut
                    sélectionner, notamment CLIP et DINO. Ces technologies permettent à Panoptic de regrouper
                    automatiquement des images similaires, d’effectuer des recherches en langage naturel par reconnaissance
                    de contenu et de trier les images de manière efficace. L’un des principaux atouts de Panoptic réside
                    dans sa capacité à associer des annotations et des étiquettes aux images, offrant ainsi un outil adapté
                    aux besoins de documentation des collections.
                </p>
               ''')               
                
        
    with tab3:
        st.html(''' <h2>Reconnaissance et transcription de textes imprimés et manuscrits</h2>
            <p>Cette section décrira les usages possibles de technologies IA pour automatiser la reconnaissance de
            caractères dans des documents numérisés. L'OCR (Optical Character Recognition) et l'HTR (Handwritten
            Text Recognition) sont des technologies qui ont beaucoup évolués ces dernières années grâce aux progrès
            de l'IA, et en particulier du deep learning. De
            nombreux
            outils et applications sont désormais disponibles pour automatiser la reconnaissance de caractères dans
            des documents imprimés ou manuscrits, avec des niveaux de performance très élevés. </p>
            <h3>Tour d'horizon rapide</h3>
            <p>Ce sont des technologies plus anciennes et plus éprouvées que celles de vision par ordinateur ou d'IA
            génératives et elles se séparent donc en deux grandes catégories : l'OCR et l'HTR.
            Concernant l'HTR nous pouvons citer des outils comme Kraken
            qui
            offrent une solution complète de l'installation, aux premiers travaux de reconnaissances jusqu'au
            ré-entrainement pour fine-tuning et l'export massif.</p>
            <p>Ou bien des solutions commeTranskribus ou eScriptorium proposent des interfaces utilisateurs
            et des
            performances élevées.</p>
            <p>Ensuite, pour l'OCR beaucoup d'outils existent mais nous mentionnons l'existence de deux projets
            performants PeroOCR et Tesseract qui offrent des bons résultats complètement gratuitements</p>''')
        st.image(image=image_path(liste_images, "HTR_Calfa_BnF.png"), caption="capture d'écran montrant un résultat d'HTR sur des textes arabes manuscrits")
        st.html('''<h3>Mise en place</h3>
            <p>La mise en place de ces technologies dépendra de vos besoins, de vos compétences techniques et de vos
            ressources matérielles. Pour des besoins ponctuels ou des volumes limités, des solutions en ligne comme
            Transkribus peuvent être suffisantes. Pour des besoins plus importants ou des exigences spécifiques,
            l'installation locale de Kraken ou Tesseract peut être nécessaire.</p>
            <p>Il est important de noter que la qualité des résultats dépendra fortement de la qualité des images
            numérisées et de la spécificité des documents (langue, écriture, mise en page). Dans certains cas, un
            ré-entrainement du modèle peut être nécessaire pour obtenir des résultats satisfaisants.</p>
            <p>En terme d'infrastructures des <a href="/pages/lexique.html#GPU">GPU</a> risquent d'être nécessaires pour
            les
            larges corpus (au-delà de 1000 pages). Pour les moyens humains, il faut avoir en tête qu'avoir une
            personne qui parle la langue, ou lit l'écriture du siècle en question est souvent indispensable pour le
            réentrainement. Du côté technique, les applications ne sont pas excessivement compliquées et elles sont
            bien documentées, mais leur manipulation requiert un minimum d'aisance avec l'informatique.</p>''')
        st.image(image=image_path(liste_images, "OCR_Hugo_BnF.png"), caption="capture d'écran montrant un résultat d'un OCR sur un texte de Victor Hugo")

            

    
    tab4.html("""<body> à voir </body>""")

page_names_to_func = {"Accueil": accueil,
                      "Lexique": lexique,
                      "Usages de l'IA": usages}
demo_name = st.sidebar.selectbox("Sélectionnez la page qui vous intéresse", page_names_to_func.keys())
page_names_to_func[demo_name]()