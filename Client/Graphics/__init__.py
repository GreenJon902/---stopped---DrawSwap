import os

from kivy.logger import Logger
from kivy.factory import Factory
from kivy.lang import Builder

import AppInfo
from Graphics.drawSwap import DrawSwap


def load_kv():
    for filename in os.listdir(AppInfo.kv_language_dir):
        Builder.load_file(os.path.join(AppInfo.kv_language_dir, filename))
        Logger.debug("kv_loader: Loaded " + str(filename))


def setup():
    from Graphics.Screens.splashScreen import SplashScreen
    from Graphics.Screens.titleScreen import TitleScreen
    from Graphics.Screens.playScreen import PlayScreen
    from Graphics.drawSwapScreenManager import DrawSwapScreenManager
    from Graphics.hoverButton import HoverButton

    Factory.register("DrawSwapScreenManager", cls=DrawSwapScreenManager)
    Factory.register("HoverButton", cls=HoverButton)
    Factory.register("DrawSwap", cls=DrawSwap)
    Factory.register("SplashScreen", cls=SplashScreen)
    Factory.register("TitleScreen", cls=TitleScreen)
    Factory.register("PlayScreen", cls=PlayScreen)

    Logger.info("All classes have been assigned to Factory")


def start():
    Logger.info("Graphics are starting")

    app = DrawSwap()
    app.run()

    Logger.info("Graphics have ended")
