import logging
import logging.config

def get_logger(name, level=logging.INFO, conf_file_loc="../conf/logging.yml"):
    """
    Python logger object with reasonable defaults.
    Uses hard-coded configuration in absence of PyYAML or the configuration file.

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

    # Check if can load yaml or if the file exists
    try:
        import yaml

        with open(conf_file_loc, "r") as f:
            config = yaml.safe_load(f.read())

    except:
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
                    "filename": "../logs/logoutput.log",
                    "formatter": "detailed",
                    "maxBytes": 4096,
                },
            },
            "root": {"handlers": ["console", "file"], "level": "DEBUG"},
            "version": 1,
        }

    logging.config.dictConfig(config)
    logger = logging.getLogger(name)
    logger.setLevel(level) 

    return logger

