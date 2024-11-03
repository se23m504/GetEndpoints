import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE")
API_HOST = os.getenv("API_HOST")
SERVICE_NAME = os.getenv("SERVICE_NAME")
SERVICE_TYPE = os.getenv("SERVICE_TYPE")
SERVICE_IP = os.getenv("SERVICE_IP")
SERVICE_PORT = os.getenv("SERVICE_PORT")
