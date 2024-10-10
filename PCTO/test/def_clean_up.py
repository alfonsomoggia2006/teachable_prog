import os
import shutil
import logging
from typing import BinaryIO

# Set up logger
logger = logging.getLogger(__name__)

def clean_up(base_path: str) -> None:

    file_list = os.listdir(base_path)
    for file_name in file_list:
        file_path = os.path.join(base_path, file_name)
        try:
            os.remove(file_path)
            logger.debug(f"Removed file: {file_path}")
        except Exception as e:
            logger.error(f"Error removing file {file_path}: {str(e)}")

def create_save_location(save_location: str) -> None:

    os.makedirs(save_location, exist_ok=True)
    logger.info("Creation of folder completed")

def save_file(file: BinaryIO, save_location: str) -> None:

    try:
        with open(save_location, "wb+") as file_object:
            shutil.copyfileobj(file, file_object)
        logger.info("File saving completed")
    except Exception as e:
        logger.error(f"Error saving file: {str(e)}")
