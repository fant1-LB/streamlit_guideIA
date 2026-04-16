import streamlit as st
from modules.data.images import image_path

def usage_chatbot_text():
    st.markdown(""" 
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
    * [Les modèles QWEN, modèles ouverts de l'entreprise chinoise Alibaba Cloud.](https://huggingface.co/Qwen) : :cn:
    """)