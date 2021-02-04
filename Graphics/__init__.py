import os

from kivy.logger import Logger
from kivy.lang import Builder

import AppInfo
from Graphics.drawSwap import DrawSwap


def load_kv():
    for filename in os.listdir(AppInfo.kv_language_dir):
        Builder.load_file(os.path.join(AppInfo.kv_language_dir, filename))
        Logger.debug("kv_loader: Loaded " + str(filename))


def start():
    Logger.info("Graphics are starting")

    app = DrawSwap()

    Logger.info("Graphics have ended")
