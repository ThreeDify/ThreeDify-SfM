import os
import logging

import requests

from threedify_sfm.models.Image import Image
from threedify_sfm.constants import API_BASE_URL

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

IMAGE_BASE_URL = "{}/images".format(API_BASE_URL)


def download(image: Image, path):
    """
    Download image to give path
    """
    filename = image.file_name
    download_url = "{}/{}".format(IMAGE_BASE_URL, filename)

    logger.info("Downloading image: %s", download_url)
    response = requests.get(download_url, stream=True)

    if response.status_code == 200:
        download_file = os.path.join(path, filename)

        logger.info("Saving image at: %s", download_file)
        with open(download_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
    else:
        logger.error("Failed to download image: %s", response.reason)
