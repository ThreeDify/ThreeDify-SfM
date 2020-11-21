import os

from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

DOWNLOAD_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "../../", "data"
)
