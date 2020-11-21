import logging
from datetime import datetime

import requests

from threedify_sfm.constants import API_BASE_URL

logger = logging.getLogger(__name__)


RECONSTRUCTIONS_API_URL = "{}/reconstructions".format(API_BASE_URL)


def fetch_reconstructions(limit: int = 10):
    """
    Fetch reconstruction data.

    Parameters:
    limit (int): Number of reconstructions to fetch. Default: 10

    Returns:
    list: Returns list of reconstructions json object.
    """

    try:
        logger.info("Fetching reconstructions.")
        reconstructions = requests.get(RECONSTRUCTIONS_API_URL).json()
        logger.info("Fetched %d reconstructions.", len(reconstructions))

        # TODO: Add sorting as request param when API supports.
        reconstructions = sorted(
            reconstructions,
            key=lambda x: datetime.strptime(
                x.get("createdAt"), "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
        )

        # TODO: Add limits as request param when API supports.
        return reconstructions[0:limit]
    except ValueError as err:
        logger.error("Error occurred while fetching reconstructions: %s", err)

    return []
