from transformers import T5ForConditionalGeneration, AutoTokenizer, pipeline
from app.config import Config

class NLPModel:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained(
            "google/flan-t5-base", cache_dir=Config.MODEL_CACHE_DIR
        )
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.qa_pipeline = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer
        )
    def answer_question(self, question: str, context: str) -> str:
        input_text = f"question: {question} context: {context}"
        return self.qa_pipeline(input_text, max_length=200)[0]["generated_text"]
