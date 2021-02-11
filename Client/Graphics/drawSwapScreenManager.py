from kivy import Logger
from kivy.uix.screenmanager import ScreenManager
from kivy.uix import screenmanager

import staticConfigurables


class DrawSwapScreenManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        super(DrawSwapScreenManager, self).__init__(*args, **kwargs)

        Logger.info("ScreenManager: Using" + str(staticConfigurables.graphics.get("General", "transition")))
        self.transition = screenmanager.__dict__[str(staticConfigurables.graphics.get("General", "transition"))]()

        self.current = "TitleScreen"

    def set_screen(self, screen_name):
        self.current = screen_name

        Logger.info("ScreenManager: Switched to " + str(screen_name))
