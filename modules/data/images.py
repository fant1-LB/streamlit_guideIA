import re
from pathlib import Path

def is_valid_url(url: str) -> bool:
    pattern = re.compile(
        r"^(https?:\/\/)"
        r"(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})"
        r"(\/.*)?$"
    )
    return bool(pattern.match(url))

def image_path(image_name, base_dir=Path("data/images")):
    path = base_dir / image_name
    return path if path.exists() else None
