"""logger module."""

from logging import Logger, StreamHandler, getLogger

LoggerLevelT = int


def get_logger(name: str, level: LoggerLevelT) -> Logger:
    """Get logger with specified name and level."""
    logger = getLogger(name)
    handler = StreamHandler()
    handler.setLevel(level)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
