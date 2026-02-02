# examples/make_music.py

import os
import argparse
from ai_content.generator import create_music
from dotenv import load_dotenv
load_dotenv()  # This reads the .env file
# Load Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found in environment. Music generation may fail.")
else:
    print("Gemini API key loaded successfully!")

# Set up command-line arguments
parser = argparse.ArgumentParser(description="Generate music using AI content providers.")
parser.add_argument("--provider", type=str, default="lyria", help="Music provider to use (default: lyria)")
parser.add_argument("--duration", type=int, default=30, help="Duration of music in seconds (default: 30)")
args = parser.parse_args()

# Generate music
try:
    filename = create_music(provider_name=args.provider, duration=args.duration)
    print(f"Music generated successfully: {filename}")
except Exception as e:
    print(f"Error generating music: {e}")

