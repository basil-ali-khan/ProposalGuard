import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db_data")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
    AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

