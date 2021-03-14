import os
import sqlite3

import config
from config import Config
from loggerFunctions import info
from sql_commands import make_new_users_table

import logging

logger = logging.getLogger("sql")


def make_new():
    info(logger, "Making new sql")
    conn = sqlite3.connect(os.path.join(config.save_folder, Config.get("Database", "name")))
    c = conn.cursor()
    info(logger, "Successfully connected to the database")

    c.execute(make_new_users_table)

    conn.commit()
    info(logger, "Successfully ran and committed sql")
