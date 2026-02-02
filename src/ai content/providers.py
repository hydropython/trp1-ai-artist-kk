# Custom minimal provider list
PROVIDERS = {
    "jazzlyria": {"type": "music", "vocals": False, "style": "jazz"},
    "popminimax": {"type": "music", "vocals": True, "style": "pop"},
    "natureveo": {"type": "video", "image_to_video": True, "style": "nature"}
}

def list_providers():
    return [name for name in PROVIDERS]
