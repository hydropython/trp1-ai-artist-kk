import os
from ai_content.generator import create_video

# Load API key (if any video provider requires it)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(f"Gemini API key loaded: {GEMINI_API_KEY is not None}")

# Generate video using the 'veo' provider
try:
    filename = create_video(provider_name="veo", duration=5)
    print(f"Video generated successfully: {filename}")
except Exception as e:
    print(f"Error generating video: {e}")
