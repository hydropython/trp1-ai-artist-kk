from src.ai_content.generator import create_video

# Generate a unique video file
video_file = create_video("natureveo", duration=8)
print(f"Your video file: {video_file}")
