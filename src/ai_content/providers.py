PROVIDERS = {
    "lyria": {"type": "music", "style": "jazz"},        # Instrumental music provider
    "minimax": {"type": "music", "style": "pop"},       # Music with vocals
    "veo": {"type": "video", "style": "nature"},        # Video provider
}

def list_providers():
    return [name for name in PROVIDERS]
