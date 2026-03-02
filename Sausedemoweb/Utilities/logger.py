import logging
import os

def get_logger():

    log_folder = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, "test.log")

    logger = logging.getLogger("SauceDemoLogger")
    logger.setLevel(logging.INFO)

    # Remove old handlers (important for pytest)
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger