# src/ai_content/generator.py
from .providers import PROVIDERS
from .utils import log_action

def create_music(provider_name, duration=20):
    provider = PROVIDERS.get(provider_name)
    if not provider or provider["type"] != "music":
        raise ValueError("Invalid music provider")
    filename = f"{provider_name}_{provider['style']}_{duration}s.wav"
    log_action(f"Generated music: {filename}")
    return filename

def create_video(provider_name, duration=5):
    provider = PROVIDERS.get(provider_name)
    if not provider or provider["type"] != "video":
        raise ValueError("Invalid video provider")
    filename = f"{provider_name}_{provider['style']}_{duration}s.mp4"
    log_action(f"Generated video: {filename}")
    return filename

