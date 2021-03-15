import random

from kivy.logger import Logger

import AppInfo
from Connection.sendRecv import send, recv
from settings import Settings


def new_uuid(s):
    Logger.info("Connection: Generating new password and asking for uuid")

    password = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                                     ) for i in range(16))
    Settings.set("Account", "password", password)
    Logger.info("Connection: Saved password")

    send(s, "1")
    Logger.info("Connection: New uuid requested")

    new_uuid = recv(s)
    Logger.info("Connection: New uuid us " + str(new_uuid))
    Settings.set("Account", "uuid", str(new_uuid))
    Logger.info("Connection: New uuid received and saved")

    send(s, password)
    Logger.info("Connection: Sent password")

    with open(AppInfo.settings_file, 'w') as settingsfile:  # save
        Settings.write(settingsfile)
    Logger.info("Connection: Saved uuid and password")


__all__ = ["new_uuid"]
