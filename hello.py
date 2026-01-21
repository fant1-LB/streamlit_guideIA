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
    
page_names_to_func = {"Accueil": accueil,
                      "Lexique": lexique}
demo_name = st.sidebar.selectbox("Sélectionnez la page qui vous intéresse", page_names_to_func.keys())
page_names_to_func[demo_name]()