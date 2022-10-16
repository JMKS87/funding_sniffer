import logging

FETCH_INTERVAL = 120
DATA_DIR = "data"

def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("info.log"), logging.StreamHandler()],
    )
