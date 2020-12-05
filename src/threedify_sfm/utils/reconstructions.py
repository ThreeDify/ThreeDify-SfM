import sys
import logging
from typing import List

import requests

from threedify_sfm.constants import API_BASE_URL
from threedify_sfm.models.Reconstruction import Reconstruction

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


RECONSTRUCTIONS_API_URL = "{}/reconstructions/batch".format(API_BASE_URL)
RECONSTRUCTIONS_FAILED_URL = "{}/reconstructions/{}/failed".format(API_BASE_URL, "{}")
RECONSTRUCTIONS_SUCCESS_URL = "{}/reconstructions/{}/success".format(API_BASE_URL, "{}")


def fetch_reconstructions(limit: int = 10) -> List[Reconstruction]:
    """
    Fetch reconstruction data.

    Parameters:
    limit (int): Number of reconstructions to fetch. Default: 10

    Returns:
    list: Returns list of reconstructions json object.
    """

    params = {"size": limit}

    try:
        logger.info("Fetching reconstructions.")
        response = requests.put(RECONSTRUCTIONS_API_URL, params=params)
        if response.status_code == 200:
            reconstructions = response.json()
            logger.info("Fetched %d reconstructions.", len(reconstructions))

            return [Reconstruction.parse(recon) for recon in reconstructions]

        logger.info("No reconstructions in queue.")
    except:
        err = sys.exc_info()[0]
        logger.error("Error occurred while fetching reconstructions: %s", err)

    return []


def reconstruction_failed(reconstruction: Reconstruction):
    """
    Reset reconstruction process.

    Parameters:
    reconstruction (Reconstruction): Reconstruction to reset.
    """
    try:
        logger.info("Reseting reconstruction: %d", reconstruction.id)
        response = requests.put(RECONSTRUCTIONS_FAILED_URL.format(reconstruction.id))
        if response.status_code == 200:
            logger.info("Reconstrucion %d reset completed.", reconstruction.id)
        else:
            logger.info("Reconsturction with id %d doesn't exists.", reconstruction.id)
    except:
        err = sys.exc_info()[0]
        logger.error("Error occurred while reseting reconstructions: %s", err)


def reconstruction_success(reconstruction: Reconstruction, file_path: str):
    """
    Reset reconstruction process.

    Parameters:
    reconstruction (Reconstruction): Reconstruction to reset.
    file_path (str): Path to reconstruction output file.
    """
    try:
        files = {"reconstruction_file": open(file_path, "rb")}

        logger.info(
            "Uploading reconstruction output (%s) for: %d", file_path, reconstruction.id
        )
        response = requests.put(
            RECONSTRUCTIONS_SUCCESS_URL.format(reconstruction.id), files=files
        )
        if response.status_code == 200:
            logger.info(
                "Reconstrucion output uploaded successfully for: %d", reconstruction.id
            )
        else:
            response.raise_for_status()
    except:
        err = sys.exc_info()[0]
        logger.error("Error occurred while reseting reconstructions: %s", err)
        raise
