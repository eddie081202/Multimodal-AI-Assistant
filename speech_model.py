import whisper
from app.config import Config

class SpeechModel:
    def __init__(self):
        self.model = whisper.load_model(
            "base",
            download_root=Config.MODEL_CACHE_DIR
        )
    
    def transcribe(self, audio_path: str) -> str:
        result = self.model.transcribe(audio_path)
        return result["text"]
