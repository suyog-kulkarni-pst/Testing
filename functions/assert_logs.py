import logging

logger = logging.getLogger("assert_logs.py")

def assert_logs():
    logger.warning("warning from main.py")