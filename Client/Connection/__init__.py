from kivy.logger import Logger

from Connection.functions import connect_to_server


def join_public():
    Logger.info("Connection: Joining a public game")

    connect_to_server()


__all__ = ["join_public"]
