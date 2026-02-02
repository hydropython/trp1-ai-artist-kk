# TRP1 Task 2 Submission

## Environment Setup
- No real APIs needed yet
- Python scripts run locally in virtual environment
- GEMINI_API_KEY loaded successfully for simulation

## Codebase Understanding
- `providers.py` stores provider options
- `generator.py` handles file creation (`create_music` & `create_video`)
- `utils.py` logs actions
- `examples/make_music.py` and `examples/make_video.py` test functionality

## Generation Log
- Music generated: `lyria_jazz_30s.wav`
- Video generated: `veo_nature_5s.mp4`

## Challenges & Solutions
- `uv-cli` not installed → skipped CLI; ran scripts directly
- Circular import / module errors → used function calls only
- Environment variables → ensured GEMINI_API_KEY loaded

## Insights & Learnings
- Small, modular design allows easy extension
- Providers and generator are decoupled
- Clear separation between configuration, generation, and logging

## Submission Links
- **YouTube Link(s):** _[Insert YouTube video links here]_
- **GitHub Repository:** [https://github.com/hydropython/trp1-ai-artist-kk](https://github.com/hydropython/trp1-ai-artist-kk)
