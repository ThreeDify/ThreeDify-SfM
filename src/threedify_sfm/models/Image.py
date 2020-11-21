class Image:
    id: int
    file_name: str
    mime_type: str

    @staticmethod
    def parse(data):
        """
        Parse Image object from json data.
        """
        image = Image()

        image.id = data.get("id")
        image.file_name = data.get("fileName")
        image.mime_type = data.get("mimetype")

        return image
