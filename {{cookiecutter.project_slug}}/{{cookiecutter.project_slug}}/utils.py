import logging
import logging.config
from pathlib import Path

wd = Path(__file__).parent.resolve()


def get_logger(name, level=logging.INFO, conf_file_loc=wd / "../conf/logging.yml"):
    """
    Python logger object with reasonable defaults.
    Writes to `logs/NAME.log`

    Usage
    -----
    >>> logger = get_logger(__name__)
    >>> logger.info("Hello there!")

    Args
    ----
    fname: string
        Name to pass to logging.getLogger. Typically
        __name__ is passed.

    Returns
    -------
    logger: Python logger object
    """
    if name is None:
        name = "root"

    # If not possible, use hard-coded configuration
    config = {
        "formatters": {
            "detailed": {
                "datefmt": "%Y-%m-%d %H:%M:%S+%z",
                "format": "%(asctime)s | %(name)s | (%(levelname)s) | %(message)s",
            },
            "simple": {
                "datefmt": "%Y-%m-%d %H:%M:%S+%z",
                "format": "(%(levelname)s): %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": "DEBUG",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "backupCount": 3,
                "class": "logging.handlers.RotatingFileHandler",
                "filename": wd / f"../logs/{name}.log",
                "formatter": "detailed",
                "maxBytes": 10485760,  # 10 MB
                "level": "DEBUG",
            },
        },
        "root": {"handlers": ["console", "file"], "level": "DEBUG"},
        "version": 1,
    }

    logging.config.dictConfig(config)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger
