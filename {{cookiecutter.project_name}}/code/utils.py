import logging


def get_logger(fname, level=logging.DEBUG):
    """
    Python logger object with reasonable defaults

    Usage
    -----
    >>> logger = get_logger(__name__, logging.INFO)
    >>> logger.info("

    Args
    ----
    fname: string
        Name to pass to logging.getLogger. Typically
        __name__ is passed.

    level: logging Level objects, or ints
        Logging level to pass to logging.setLevel().
        Ref: https://docs.python.org/3/library/logging.html#levels

    Returns
    -------
    logger: Python logger object
    """
    if name is None:
        name = "root"

    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s - %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    # Only add handlers if does not have already
    # Combined w propagate=False, prevents duplicate log msgs
    if logger.hasHandlers() is False:
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        ch.setLevel(logging.DEBUG)

    logger.propagate = False
    return logger
