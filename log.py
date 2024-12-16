import logging

RED = "\033[0;31m"
RESET = "\033[0;0m"

logger = logging.getLogger("my_logger")
logger.setLevel(logging.ERROR)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter(RED+"%(asctime)s - %(message)s"+RESET, datefmt="%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)

logger.addHandler(ch)