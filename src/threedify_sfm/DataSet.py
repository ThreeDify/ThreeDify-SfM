import os
import logging
from typing import List

from threedify_sfm.utils.images import download
from threedify_sfm.constants import DOWNLOAD_PATH
from threedify_sfm.models.Reconstruction import Reconstruction

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class DataSet:
    download_path: str
    image_paths: List[str]
    reconstruction: Reconstruction

    def __init__(self, reconstruction: Reconstruction):
        self.reconstruction = reconstruction
        self.image_paths = []

        self.download_images()

    def images(self) -> List[str]:
        """
        Get images from the dataset.
        """
        return self.image_paths

    def image_path(self) -> str:
        """
        Get the path to directory of the images.
        """
        return self.download_path

    def download_images(self):
        """
        Download images from server.
        """
        self.download_path = os.path.join(
            DOWNLOAD_PATH,
            "{}_{}".format(self.reconstruction.name, self.reconstruction.id),
            "images",
        )

        logger.info("Ensure download path exists: %s", self.download_path)
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

        logger.info("Downloading images...")
        for image in self.reconstruction.images:
            download(image, self.download_path)
            self.image_paths.append(os.path.join(self.download_path, image.file_name))
