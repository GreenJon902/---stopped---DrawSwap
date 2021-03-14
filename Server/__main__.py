import config

if __name__ == "__main__":
    import logger
    logger.rootLogger.info("Starting...")

    import logging
    mainLogger = logging.getLogger("Main")

    from loggerFunctions import info, warning
    from entrance import Entrance
    import os
    import sql

    info(mainLogger, "Imported all modules!")

    if not os.path.exists(config.save_folder):
        warning(mainLogger, "The folder ", config.save_folder, " does not exist, creating new one")
        os.makedirs(config.save_folder)
        config.make_new()
        sql.make_new()



    info(mainLogger, "Starting DrawSwap server!")

    e = Entrance()
    e.start()
    e.accept_incoming_connections()
