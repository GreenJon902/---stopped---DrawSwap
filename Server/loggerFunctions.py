def info(logger, *args):
    logger.info("".join([str(arg) for arg in args]))


def debug(logger, *args):
    logger.debug("".join([str(arg) for arg in args]))


def warning(logger, *args):
    logger.warning("".join([str(arg) for arg in args]))


def critical(logger, *args):
    logger.critical("".join([str(arg) for arg in args]))
