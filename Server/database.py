import logging
import os
from configparser import ConfigParser

import mysql.connector as mysql

import config
import sql_commands
from loggerFunctions import info, warning

logger = logging.getLogger("sql")


def execute(c, command, ignore=None):
    try:
        c.execute(command)
    except ignore as e:
        warning(logger, "\n\nIgnored sql command error: ", command, e, "\n")


def make_new(dev_mode):
    info(logger, "Making new sql")

    if not os.path.exists(os.path.join(config.save_folder, "dbLogin.ini")):

        with open(os.path.join(config.save_folder, "dbLogin.ini"), "w") as f:
            f.write(config.default_db_login)
            f.close()

        info(logger, "Create dbLogin.ini because it was not there or dev_mode was enabled")
        input("Press enter when you have entered the db login details")


    conn = connect()
    c = conn.cursor()
    info(logger, "Successfully connected to the database")

    execute(c, sql_commands.make_new_users_table, ignore=mysql.ProgrammingError)
    execute(c, sql_commands.make_new_games_table, ignore=mysql.ProgrammingError)

    conn.commit()
    info(logger, "Successfully ran and committed sql")

    conn.close()
    info(logger, "Successfully closed the connection to the database")


def connect():
    c = ConfigParser()
    c.read(os.path.join(config.save_folder, "dbLogin.ini"))
    sql_login = dict(c.items("Login"))

    conn = mysql.connect(**sql_login)

    return conn
