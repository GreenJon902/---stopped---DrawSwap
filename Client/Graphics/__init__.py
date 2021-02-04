import os

from kivy.logger import Logger
from kivy.lang import Builder

from . import drawSwap
from .. import AppInfo


def load_kv():
    for filename in os.listdir(AppInfo.kv_language_dir):
        Builder.load_file(os.path.join(AppInfo.kv_language_dir, filename))
        Logger.debug("kv_loader: Loaded " + str(filename))


def start():
    Logger.info("Graphics are starting")



    Logger.info("Graphics have ended")
