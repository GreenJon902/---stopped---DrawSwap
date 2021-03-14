import logging

import mysql.connector
from mysql.connector import DatabaseError

import config
import sql_commands
from loggerFunctions import info, warning

logger = logging.getLogger("sql")


def make_new(dev_mode):
    info(logger, "Making new sql")

    if dev_mode:
        try:
            conn = connect(no_db=True)
            c = conn.cursor()
            c.execute(sql_commands.drop_database)
            conn.commit()
            conn.close()
            info(logger, "DevMode - Database successfully connected, deleted and closed")

        except DatabaseError as e:
            warning(logger, "DevMode - Database failed to delete table -\n", e)

    conn = connect(no_db=True)
    c = conn.cursor()
    c.execute(sql_commands.create_database)
    conn.commit()
    conn.close()
    info(logger, "Database successfully connected, created and closed")

    conn = connect()
    c = conn.cursor()
    info(logger, "Successfully connected to the database")

    c.execute(sql_commands.make_new_users_table)
    c.execute(sql_commands.make_new_games_table)

    conn.commit()
    info(logger, "Successfully ran and committed sql")

    conn.close()
    info(logger, "Successfully closed the connection to the database")


def connect(no_db=False):
    sql_login = config.sql_login

    if no_db:
        sql_login = sql_login.copy()
        sql_login.pop("database")


    conn = mysql.connector.connect(**sql_login)

    return conn
