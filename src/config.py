import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE")
API_HOST = os.getenv("API_HOST")
