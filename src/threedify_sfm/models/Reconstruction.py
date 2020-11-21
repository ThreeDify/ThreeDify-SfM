from typing import List

from threedify_sfm.models.Image import Image


class Reconstruction:
    id: int
    name: str
    images: List[Image]

    @staticmethod
    def parse(data):
        """
        Parse Reconstruction object from json data
        """
        reconstruction = Reconstruction()

        reconstruction.id = data.get("id")
        reconstruction.name = data.get("name")
        reconstruction.images = [Image.parse(img) for img in data.get("images")]

        return reconstruction
