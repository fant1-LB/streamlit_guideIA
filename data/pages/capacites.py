import streamlit as st
from pathlib import Path

from modules.data.images import image_path
from modules.data.load_data import load_markdown

from data.pages.usages_ia.description import usage_description_text
from data.pages.usages_ia.navigation import usage_navigation_text
from data.pages.usages_ia.transcription import usage_transcription_text
from data.pages.usages_ia.chatbot import usage_chatbot_text

def capacites():
    load_markdown("data/pages/usages_ia/presentation.md")
    with st.container(border=True):
        load_markdown("data/pages/usages_ia/legende.md")

    st.set_page_config(layout="wide",)
    tab1, tab2, tab3, tab4 = st.tabs(["Description et classification d'images", "Exploration de grands corpus d'images", "Transcription de textes", "Chatbots et assimilés"])
    
    with tab1:
        usage_description_text()

    with tab2: 
        usage_navigation_text()
                        
    with tab3:
        usage_transcription_text()

    with tab4:
        usage_chatbot_text()
