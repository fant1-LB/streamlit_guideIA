def is_valid_url(url: str) -> bool:
    pattern = re.compile(
        r"^(https?:\/\/)"
        r"(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})"
        r"(\/.*)?$"
    )
    return bool(pattern.match(url))
