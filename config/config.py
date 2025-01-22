import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application configurations
APP_NAME = "JobSync"
APP_VERSION = "1.0.0"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POPPLER_PATH = os.path.join(BASE_DIR, "../poppler-24.08.0")
ASSETS_PATH = os.path.join(BASE_DIR, "../assets")

# Environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Default values
DEFAULT_LANGUAGE = "en"
DEFAULT_OUTPUT_FOLDER = os.path.join(BASE_DIR, "../output")
