from pathlib import Path
def image_path(liste_images, image_name):
    for i in liste_images:
        if Path(i).name== image_name:
            return Path(i)