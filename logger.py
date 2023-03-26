import logging
from logging.handlers import RotatingFileHandler
import inspect

def get_logger(__name__):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Check if the logger already has handlers to avoid adding duplicate handlers
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')

        # Set up a rotating file handler
        file_handler = RotatingFileHandler('app.log', maxBytes=1024*1024*10, backupCount=1) # 10 mb
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)

        logger.addHandler(file_handler)

    return logger

