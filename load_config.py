import os
from typing import Tuple
from dotenv import load_dotenv


def load_config() -> Tuple[str, str, float]:
    load_dotenv()
    CAMERA_URI = os.getenv("CAMERA_URI")
    CAMERA_NAME = os.getenv("CAMERA_NAME")
    INTERVAL = os.getenv("INTERVAL")

    if INTERVAL is not None:
        try:
            INTERVAL = float(INTERVAL)
        except ValueError:
            INTERVAL = 0

    return CAMERA_URI, CAMERA_NAME, INTERVAL
