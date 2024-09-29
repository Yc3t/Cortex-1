from dotenv import load_dotenv
import os 
from llama_index.embeddings.gemini import GeminiEmbedding

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# get API key and create embeddings

model_name = "models/embedding-001"

embed_model = GeminiEmbedding(
    model_name=model_name, api_key=GOOGLE_API_KEY, title="this is a document"
)

embeddings = embed_model.get_text_embedding("Google Gemini Embeddings.")


