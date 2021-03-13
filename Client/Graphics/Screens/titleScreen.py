from kivy.logger import Logger
from kivy.uix.screenmanager import Screen

from Graphics.screenWhichIncludesHoverButton import ScreenWhichIncludesHoverButton


class TitleScreen(Screen, ScreenWhichIncludesHoverButton):
    content_image = None


    def play_button_pressed(self):
        self.content_image = self.ids["content"].export_as_image().texture
        self.content_image.uvpos = (0, 1)
        self.content_image.uvsize = (1, -1)
        Logger.info("TitleScreen: Content exported as image for play screen")

        self.parent.set_screen("JoinGameScreen")
