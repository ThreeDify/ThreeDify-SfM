import os
import logging

from opensfm import dataset
from opensfm.actions import (
    extract_metadata,
    detect_features,
    match_features,
    create_tracks,
    reconstruct,
    mesh,
    undistort,
    compute_depthmaps,
)

from threedify_sfm.DataSet import DataSet

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class OpenSfM:
    """
    Run structure from motion pipeline on given dataset.
    """

    sub_folder: str
    dataset: dataset.DataSet

    def __init__(self, data: DataSet):
        self.dataset = dataset.DataSet(data.data_path())
        self.sub_folder = "undistored"

    def run(self):
        """
        Run the SFM pipeline
        """
        logger.info("Running SFM pipeline.")

        logger.info("Extracting camera data from dataset.")
        extract_metadata.run_dataset(self.dataset)

        logger.info("Extracting features from dataset.")
        detect_features.run_dataset(self.dataset)

        logger.info("Matching features from the images in the dataset.")
        match_features.run_dataset(self.dataset)

        logger.info("Creating tracks from the matches.")
        create_tracks.run_dataset(self.dataset)

        logger.info("Running reconstruction.")
        reconstruct.run_dataset(self.dataset)

        logger.info("Generating mesh.")
        mesh.run_dataset(self.dataset)

        logger.info("Undistoring images.")
        undistort.run_dataset(self.dataset, None, 0, None, self.sub_folder)

        logger.info("Computing depthmaps.")
        compute_depthmaps.run_dataset(self.dataset, self.sub_folder, False)

        return os.path.join(
            self.dataset.data_path, self.sub_folder, "depthmaps", "merged.ply"
        )
