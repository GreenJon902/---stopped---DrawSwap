if __name__ == "__main__":
    import logger
    logger.rootLogger.info("Starting...")

    import logging
    mainLogger = logging.getLogger("Main")

    from loggerFunctions import info
    from entrance import Entrance

    info(mainLogger, "Imported all modules!")

    info(mainLogger, "Starting DrawSwap server!")

    e = Entrance()
    e.start()
    e.accept_incoming_connections()
