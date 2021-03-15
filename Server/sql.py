import logging
import os
from configparser import ConfigParser

import mysql.connector

import config
import sql_commands
from loggerFunctions import info

logger = logging.getLogger("sql")


def make_new(dev_mode):
    info(logger, "Making new sql")

    if not os.path.exists(os.path.join(config.save_folder, "dbLogin.ini")):

        with open(os.path.join(config.save_folder, "dbLogin.ini"), "w") as f:
            f.write(config.default_db_login)

        info(logger, "Create dbLogin.ini because it was not there or dev_mode was enabled")
        input("Press enter when you have entered the db login details")


    conn = connect()
    c = conn.cursor()
    info(logger, "Successfully connected to the database")

    c.execute(sql_commands.make_new_users_table)
    c.execute(sql_commands.make_new_games_table)

    conn.commit()
    info(logger, "Successfully ran and committed sql")

    conn.close()
    info(logger, "Successfully closed the connection to the database")


def connect():
    c = ConfigParser()
    c.read(os.path.join(config.save_folder, "dbLogin.ini"))
    sql_login = c.options("Login")
    print(sql_login)

    conn = mysql.connector.connect(**sql_login)

    return conn
