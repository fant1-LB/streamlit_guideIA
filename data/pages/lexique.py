import streamlit as st

def lexique():
    st.html('''<h3 id="API">API</h3>
            <p>Une API, pour <i>application programming interface</i> ou « interface de programmation d'application »
                est un système qui permet de connecter un logiciel à une machine en ligne. Les APIs permettent par exemple d'envoyer sur un serveur extérieur des
                requêtes à des modèles d'IA trop lourds pour fonctionner sur un ordinateur ou serveur de l'institution.
                Un traitement qui implique de faire appel à une API implique donc l'accès par un acteur extérieur à l'institution aux documents traités, et donc une vigilance particulière quant au régime de droit des documents en question.
                La plupart des grands <i>Large language models</i> (LLM) commerciaux peuvent être utilisés via leur API. </p>''')
            
    st.html('''<h3 id="Annotations">Annotations</h3>
            <p>Dans un contexte IA, les annotations sont les données que l’on va utiliser pour entraîner ou réentrainer
                un modèle. La forme de l’annotation dépend du modèle que l’on veut entraîner ou réentrainer. La
                transcription d’une zone de texte est une annotation dans un contexte d’OCR/HTR. Un “tag” associé à
                l’image est une annotation pour un modèle de classification. Une zone délimitée sur une image est une
                annotation pour un modèle de segmentation. Obtenir des annotations de qualité est un enjeu primordial
                dans n’importe quel projet IA.</p>''')
            
    st.html('''<h3 id="chatbot">ChatBot ou agent conversationnel</h3>
            <p>Un chatbot est un logiciel conçu pour interagir avec un utilisateur au travers d’échanges textuels ou
                vocaux. Cette technologie préexiste aux LLMs et à l’émergence de l’IA mais a passé un cap en étant
                associés à des LLMs. Grâce à eux le chatbot peut converser avec l’utilisateur dans un langage naturel.
                C’est probablement l’application de l’IA la plus connue du grand public. Un chatbot IA est souvent nommé
                d’après le modèle qui le fait fonctionner.<br>
                Ex : ChatGPT, Le Chat (Mistral), Claude, Gemini…</p>''')
            
    st.html('''<h3 id="computerVision">Computer vision</h3>
            <p>La <em>Computer Vision</em> ou vision par ordinateur en français, sont l’ensemble des technologies
                permettant l’interprétation d’images par une machine. L’OCR, l’HTR, la segmentation d’images ou encore
                la détection d’objets sont des applications possibles de <em>Computer Vision</em>.</p>''')
            
    st.html('''<h3 id="Entraînementréentrainement">Entraînement/réentrainement</h3>
            <p>L’entraînement est le moment où l’on commence à alimenter en données un algorithme ou modèle pour qu’il
                se modifie jusqu’à atteindre les résultats qu’on désire. Un entraînement peut se faire à partir
                de données spécifiquement annotées par un humain (approche supervisée) ou brutes (approche
                non supervisée). Cette étape demande une puissance de calcul
                considérable. Le réentraînement est le fait de faire subir un nouvel entraînement à un modèle existant
                pour le modifier et l’adapter à des besoins spécifiques.</p>''')
            
    st.html('''<h3 id="Finetuning">Finetuning</h3>
            <p>Le <em>finetuning</em> est l’ensemble des manipulations que l’on fait sur un modèle pour améliorer ses
                résultats. Le <em>finetuning</em> peut passer par la modification de paramètres, d’un <em>prompt</em>,
                ou encore par un réentraînement.</p>''')
            
    st.html('''<h3 id="GPU">GPU</h3>
            <p>Un GPU, ou <em>Graphic Processing Unit</em> est une unité de calcul assurant les fonctions de traitement des
                d’images. Le GPU est le coeur de ce qu’on appelle plus couramment les cartes
                graphiques. Originellement les GPUs ont été développés pour les jeux vidéos et le calcul de trajectoires. Avec l’émergence de l’IA, la communauté scientifique s’est rendue compte qu’ils
                étaient bien plus efficaces pour le calcul des objets mathématiques (vecteurs) qu’utilisent la plupart des modèles d’IA que les
                CPUs (ou processeurs) traditionnels de nos ordinateurs. L’utilisation de GPUs accélère grandement le
                traitement par IA de données. Avoir un GPU est même nécessaire pour les modèles les plus lourds et les
                entraînements et réentraînements. </p>''')
            
    st.html('''<h3 id="LLM">LLM</h3>
            <p>Un LLM, ou grand modèle de langue, est un modèle IA capable d'interpréter et génerer du langage naturel.<br>
                Un modèle de langue est un modèle probabiliste basé sur la distribution d’éléments linguistiques (lettres,
                phonèmes, mots) dans une langue naturelle. Les plus connus sont des modèles génératifs qui calculent le
                mot suivant ou la lettre suivante le plus probablent dans une séquence de mots, selon un contexte, pour interagir avec
                l’utilisateur. Un grand modèle de langue se différencie d'un modèle de langue classique par la masse de son corpus d'entraînement et des ses paramètres, l'unité utilisée pour mesurer la taille d'un modèle d'IA.Certains LLMs sont également capables de traiter des images, on les appelle alors aussi
                des VLM (<i>vision-language model</i>).<br>
                Ex : GPT-4, DeepSeek-R1, Llama-3 …</p>''')
            
    st.html('''<h3 id="Modèle-IA">Modèle IA</h3>
            <p>Un modèle IA est un algorithme capable d’effectuer un ensemble de
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
                sortie.</p>''')
            
    st.html('''<h3 id="OCRHTR">OCR/HTR</h3>
            <p>OCR (pour <em>Optical Caracter Recognition</em>) et HTR (pour <em>Handwritten Text Recognition</em>)
                sont les noms données à la transcription automatique de texte imprimé (pour l’OCR) et manuscrit (pour
                l’HTR). Ces deux technologies peuvent être rassemblées sous le terme d'"ATR", pour <em> Automatic Text Recognition </em> <br>
                Ex : Tesseract-ocr, pero-ocr, monkey-ocr…</p>''')
            
    st.html('''<h3 id ="Plongement">Plongement </h3>
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
            </p>''')
            
    st.html('''<h3 id="segmentation">Segmentation</h3>
            <p>La segmentation est une technique qui consiste à diviser une image en zones distinctes, auxquelles peuvent être associées des classes. Cette technique est particulièrement utile pour repérer la présence où non d'éléments dans une 
            image, et plus généralement pour l'analyse d'images par IA.</p>''')
            
    st.html('''<h3 id="VLM">VLM</h3>
            <p>Un VLM (ou <em>Vision Language Model</em>) est un modèle IA proche du LLM, mais capable de traiter simultanément du texte et des 
            images. Contrairement aux modèles de vision par ordinateur traditionnels qui se 
            limitent à classifier ou détecter des objets, les VLM peuvent raisonner sur le contenu visuel et répondre à des questions 
            ouvertes en langage naturel. Ces modèles permettent la description d'images, la compréhension de documents structurés ou la recherche sémantique avancée dans des images.
            </p>
            ''')