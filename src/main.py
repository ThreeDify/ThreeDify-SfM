import logging

from threedify_sfm.SfM import SfM
from threedify_sfm.DataSet import DataSet
from threedify_sfm.utils.opensfm import OpenSfM
from threedify_sfm.constants import SFM_IMPLEMENTATION
from threedify_sfm.utils.reconstructions import fetch_reconstructions

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    reconstructions = fetch_reconstructions()

    for reconstruction in reconstructions:
        logger.info(
            "Running SfM for reconstruction: %s (%s)",
            reconstruction.id,
            reconstruction.name,
        )

        logger.info("Creating dataset for reconstruction.")
        dataset = DataSet(reconstruction)

        if SFM_IMPLEMENTATION == "OPENSFM":
            logger.info("Using OpenSfM implementation.")
            sfm = OpenSfM(dataset)
        else:
            logger.info("Using ThreeDify SfM implementation.")
            sfm = SfM(dataset)

        logger.info("Running SfM pipeline.")
        sfm.run()


if __name__ == "__main__":
    main()
