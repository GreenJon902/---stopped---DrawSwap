import os
import shutil

import config

if __name__ == "__main__":
    if config.dev_mode:
        print("Dev mode activated")

        shutil.rmtree(config.save_folder)

    make_new = True #TESTING PURPOSES
    if not os.path.exists(config.save_folder) or make_new:
        print("Save folder is not here, making a new one")

        make_new = True
        try:
            os.makedirs(config.save_folder)
            os.makedirs(config.log_folder)
        except FileExistsError:
            print("Cant make folder, already exists")
        config.make_new(config.dev_mode)

    import logger

    logger.rootLogger.info("Starting...")

    import logging

    mainLogger = logging.getLogger("Main")

    from loggerFunctions import info
    from entrance import Entrance
    import database

    info(mainLogger, "Imported all modules!")

    if make_new:
        database.make_new(config.dev_mode)

    info(mainLogger, "Starting DrawSwap server!")

    e = Entrance()
    e.start()
    e.accept_incoming_connections()
