import streamlit as st
from modules.data.images import image_path

def usage_chatbot_text():
    st.markdown(""" 
    ### Agents conversationnels (chatbots) et interactions en langage naturelle

    #### Définition des agents conversationnels            
    Les chatbots représentent aujourd’hui l’une des applications du *machine learning* les plus visibles et les plus largement diffusées dans l’espace public.
    Un agent conversationnel est un système informatique conçu pour dialoguer avec un utilisateur en langage naturel, généralement sous la forme d’un échange de questions et de réponses. Ces outils s’appuient sur des modèles de langage de grande taille (*Large Language Models*), capables de comprendre, générer et structurer du texte de manière cohérente. La plupart des chatbots modernes sont polyvalents (ou généralistes) et peuvent être utilisés dans des contextes variés : information, assistance, rédaction ou encore programmation. Parmi les exemples les plus connus figurent ChatGPT (OpenAI), Claude (Anthropic), Le Chat (Mistral) et Gemini (Google). Les grands modèles de langue derrière ces agents conversationnels sont entraîné sur une grande quantité de texte pour être capable de produire du langage dans le plus de contextes différents possibles.
    
    #### Specialiser des agents conversationnels
    Afin d'éviter des hallucinations sur des sujets trop complexes ou d'éviter de réentraîner des modèles, une tâche coûteuse en ressources, ces agent conversationnels peuvent être adaptés pour s'appuyer sur des données supplémentaires consacrées à un sujet précis en complément de leur corpus d'entraînement originel lorsqu'ils génèrent leurs réponses. Ainsi, le modèle accède à un ensemble de textes, des documents ou une base de données et utilisent ces informations comme source de référence pour construire ses réponses, ce qui améliore leur fiabilité et leur pertinence. Cette approche est connue sous le nom de *Retrieval-Augmented Generation¨ (RAG). D’autres techniques poursuivent des objectifs similaires, comme les [LoRa](https://www.ibm.com/think/topics/lora) (Low-Rank Adaptation), qui permettent d’adapter un modèle à moindre coût, ou encore le [MCP](https://www.ibm.com/fr-fr/think/topics/model-context-protocol) (Model Context Protocol), qui facilite l’intégration et l’exploitation de sources de données externes dans le processus de génération.
                    
    #### Les Chatbot dans les institutions patrimoniales
                    
    Dans le contexte des institutions patrimoniales, les agents conversationnels offrent une diversité d’usages. Mis à disposition du public, ils peuvent servir d’outils de médiation, fournir des informations sur l’institution ou encore faciliter l’exploration des collections. En interne, ils peuvent également accompagner les équipes dans certaines tâches administratives, ainsi que dans la consultation et l’analyse de bases de données ou de corpus documentaires. Dans ces différents cas, il ne s’agit généralement pas de réentraîner entièrement les modèles, mais plutôt de les spécialiser, afin de limiter la complexité technique et les coûts d’ingénierie.

    Par ailleurs, les modèles de langage derrière les chatbot nécessitent des infrastructures de calcul importantes, notamment des GPU, ce qui rend leur déploiement local dans les institutions complexe. En conséquence, de nombreuses solutions de chatbot « clés en main » reposent sur des API, c’est-à-dire des services externes permettant d’interroger des modèles hébergés sur des serveurs disposant de cette puissance de calcul. Le recours à ces API implique une circulation des données en dehors de l’institution, voire à l’international, ce qui soulève des enjeux juridiques, éthiques et de souveraineté des données qu’il est essentiel d’anticiper.

    ### Outils et ressources 
    * [NotebookLM, outil integré de google pour interroger des documents à l'aide des modèles Gemini](https://notebooklm.google/) : :us: - :lock: - :free:/:moneybag:    
    * [Ollama, outil de déploiement de LLMs en local](https://ollama.com/) : :us: - :unlock: - :free:/:moneybag:

    ### Exemples de modèles               
    * [La série des modèles Mistral, de l'entreprise française Mistral AI. Il en existe de plusieurs tailles et un certain nombre de modèles spécialisés (Mistral OCR, Voxtral...)](https://huggingface.co/mistralai) : :fr:
    * [Les modèles Gemma, modèles ouverts de Google, conçus pour fonctionner sans disposer d'une très grande puissance de calcul](https://deepmind.google/models/gemma/) : :us:
    * [Les modèles QWEN, modèles ouverts de l'entreprise chinoise Alibaba Cloud.](https://huggingface.co/Qwen) : :cn:
    """)