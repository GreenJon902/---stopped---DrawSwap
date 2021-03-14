import socket

from kivy.logger import Logger

from Connection import requests
from settings import Settings
from staticConfigurables import connection


def get_ip():
    return connection.get("Server", "ip")


def get_port():
    return connection.getint("Server", "port")


def connect_to_server():
    uuid = Settings.get("Account", "uuid")
    password = Settings.get("Account", "password")

    if uuid == "None":
        Logger.info("Connection: No uuid found")

        s = _connect_to_server()

        requests.new_uuid(s)
        s.close()

    return _connect_to_server()


def _connect_to_server():
    s = socket.socket()

    Logger.info("Connection: Connecting to " + str((get_ip(), get_port())))
    s.connect((get_ip(), get_port()))
    return s
