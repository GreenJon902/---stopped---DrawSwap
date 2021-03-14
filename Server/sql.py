import logging

import mysql.connector

import config
import sql_commands
from loggerFunctions import info

logger = logging.getLogger("sql")


def make_new():
    info(logger, "Making new sql")
    conn = connect()
    c = conn.cursor()
    info(logger, "Successfully connected to the database")

    c.execute(sql_commands.make_new_users_table)
    c.execute(sql_commands.make_new_games_table)

    conn.commit()
    info(logger, "Successfully ran and committed sql")


def connect():
    conn = mysql.connector.connect(**config.sql_login)

    return conn
