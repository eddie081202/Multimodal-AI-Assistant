from fastapi import FastAPI, UploadFile, Depends
from pydantic import BaseModel
from app.models.nlp_model import NLPModel
from app.models.vision_model import VisionModel
from app.models.speech_model import SpeechModel
from app.utils.database import VectorDB
from app.utils.auth import get_current_user

app = FastAPI()

# Initialize models and database
nlp = NLPModel()
vision = VisionModel()
speech = SpeechModel()
vector_db = VectorDB()

# Define request/response models
class QueryRequest(BaseModel):
    query: str
    image: bytes = None  # Optional image bytes

class ResponseModel(BaseModel):
    answer: str
    context_used: list

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Multimodal AI Assistant!"}

# /ask endpoint
@app.post("/ask", response_model=ResponseModel)
async def ask_question(
    request: QueryRequest,
    audio: UploadFile = None,
    user: dict = Depends(get_current_user)
):
    # Process audio
    if audio:
        with open("temp_audio.mp3", "wb") as f:
            f.write(await audio.read())
        request.query += speech.transcribe("temp_audio.mp3")

    # Process image
    context = []
    if request.image:
        image_embedding = vision.encode_image(request.image)
        context = vector_db.retrieve_context(image_embedding)

    # Generate answer
    answer = nlp.answer_question(request.query, " ".join(context))
    
    # Log interaction
    if user["user_id"]:
        vector_db.upsert_context(user["user_id"], image_embedding)
    
    return ResponseModel(answer=answer, context_used=context)
