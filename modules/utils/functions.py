from pathlib import Path

def image_path(image_name, base_dir=Path("data/images")):
    path = base_dir / image_name
    return path if path.exists() else None
