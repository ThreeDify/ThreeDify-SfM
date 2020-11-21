import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class DataSet:
    def __init__(self, reconstruction):
        self.reconstruction = reconstruction

    def images(self):
        """
        Get images from the dataset.
        """
        return self.reconstruction.get("images")
