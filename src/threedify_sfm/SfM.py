import logging

from threedify_sfm.DataSet import DataSet

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class SfM:
    """
    Run structure from motion pipeline on given dataset.
    """

    dataset: DataSet

    def __init__(self, dataset: DataSet):
        self.dataset = dataset

    def extract_cameras(self):
        """
        Extract camera data for the images in the dataset
        """
        logger.info("Extracting camera data from dataset.")

    def extract_features(self):
        """
        Extracts features for the images in the dataset
        """
        logger.info("Extracting features from dataset.")

    def match_features(self):
        """
        Matches features from the images in the dataset
        """
        logger.info("Matching features from the images in the dataset.")

    def create_tracks(self):
        """
        Creates tracks from the matches.
        """
        logger.info("Creating tracks from the matches.")

    def generate_base_pair(self):
        """
        Generates a pair to start reconstruction from.
        """
        logger.info("Generating base pair.")

        return (0, 1)

    def base_reconstruction(self, base_pair):
        """
        Generates base reconstruction from the initial pair.
        """
        logger.info("Generating base reconstruction from the initial pair.")

    def resection(self, view):
        """
        Estimate pose from view.
        """
        logger.info("Estimating pose from view: %s", view)

    def triangulate_view(self, view):
        """
        Triangulate a new view.
        """
        logger.info("Triangulating view: %s", view)

    def bundle_adjustment(self):
        """
        Run bundle adjustment.
        """
        logger.info("Running bundle adjustment.")

    def add_view(self, view):
        """
        Adds a new view to reconstruction.
        """
        logger.info("Adding new view to reconstruction.")

        self.resection(view)
        self.triangulate_view(view)
        self.bundle_adjustment()

    def export_as_ply(self):
        """
        Exports reconstruction as ply file.
        """
        logger.info("Exporting reconstruction as ply file.")

    def run(self):
        """
        Run the SFM pipeline
        """
        logger.info("Running SFM pipeline.")

        self.extract_cameras()
        self.extract_features()
        self.match_features()

        self.create_tracks()

        base_pair = self.generate_base_pair()
        self.base_reconstruction(base_pair)

        # TODO: Get views from tracks.
        views = []

        for view in views:
            self.add_view(view)

        self.export_as_ply()
