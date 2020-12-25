import os

from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.environ["API_BASE_URL"]

DOWNLOAD_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "../../", "data"
)

SFM_IMPLEMENTATION = os.environ.get("SFM_IMPLEMENTATION", "THREEDIFY").upper()

API_HEADERS = {
    "x-threedify-app-id": os.environ["APP_ID"],
    "x-threedify-app-secret": os.environ["APP_SECRET"],
}

BATCH_SIZE = int(os.environ.get("BATCH_SIZE", 10))
