from sentence_transformers import SentenceTransformer
from app.config import Config

class VisionModel:
    def __init__(self):
        self.model = SentenceTransformer(
            'clip-ViT-B-32',
            cache_folder=Config.MODEL_CACHE_DIR
        )

    def encode_image(self, image_bytes: bytes) -> list:
        # For simplicity, assume image_bytes is from a file upload
        return self.model.encode(image_bytes).tolist()
