import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE")
SERVICE_NAME = os.getenv("SERVICE_NAME")
SERVICE_TYPE = os.getenv("SERVICE_TYPE")
SERVICE_IP = os.getenv("SERVICE_IP")
SERVICE_PORT = os.getenv("SERVICE_PORT")
DEFAULT_ENDPOINTS = os.getenv("DEFAULT_ENDPOINTS")
LOG_LEVEL = os.getenv("LOG_LEVEL")
