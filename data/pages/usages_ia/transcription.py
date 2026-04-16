import streamlit as st
from modules.data.images import image_path

def usage_transcription_text():
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

        

    