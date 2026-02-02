from src.ai_content.generator import create_music

# Generate a unique music file
music_file = create_music("jazzlyria", duration=25)
print(f"Your music file: {music_file}")
