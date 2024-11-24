from core.constants import PROJECT_PATH
from core.logger import logger
from core.utils import start_config

if __name__ == "__main__":
    start_config()
    logger.info(f"Project path: {PROJECT_PATH}")
    logger.info("Hello world!")
