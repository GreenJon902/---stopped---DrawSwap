import random
import socket

from kivy.logger import Logger

import AppInfo
from Connection.functions import send, recv
from settings import Settings
from staticConfigurables import connection


def join_public():
    Logger.info("Connection: Joining a public game")

    connect_to_server()


def connect_to_server():
    s = socket.socket()

    Logger.info("Connection: Connecting to " + str((get_ip(), get_port())))
    s.connect((get_ip(), get_port()))

    uuid = Settings.get("Account", "uuid")
    password = Settings.get("Account", "password")

    if uuid == "None":
        Logger.info("Connection: No uuid found, generating new password and asking for uuid")

        password = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                                         ) for i in range(16))
        Settings.set("Account", "password", password)

        send(s, "1")
        Logger.info("Connection: New uuid requested")

        new_uuid = recv(s)
        Settings.set("Account", "uuid", new_uuid)
        Logger.info("Connection: New uuid received")


        send(s, password)
        Logger.info("Connection: Sent password")

        with open(AppInfo.settings_file, 'w') as settingsfile:  # save
            Settings.write(settingsfile)
        Logger.info("Connection: Saved uuid and password")





def get_ip():
    return connection.get("Server", "ip")


def get_port():
    return connection.getint("Server", "port")
