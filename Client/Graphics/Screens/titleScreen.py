from kivy.logger import Logger
from kivy.uix.screenmanager import Screen

import staticConfigurables
from Graphics.screenWhichIncludesHoverButton import ScreenWhichIncludesHoverButton


class TitleScreen(Screen, ScreenWhichIncludesHoverButton):
    content_image = None
    background_b_image = None

    def play_button_pressed(self):


        self.content_image = self.ids["content"].export_as_image().texture

        self.content_image.uvpos = (0, 1)
        self.content_image.uvsize = (1, -1)

        self.background_b_image = self.ids["background_b"].export_as_image().texture

        self.background_b_image.uvpos = (0, 1)
        self.background_b_image.uvsize = (1, -1)
        self.background_b_image = self.background_b_image.get_region(self.ids["content"].x,
                                                                     self.ids["content"].y,
                                                                     self.ids["background_b"].norm_image_size[0] *
                                                                     staticConfigurables.graphics.getfloat(
                                                                         "TitleScreen",
                                                                         "content_size_relative_to_background_b_width"),
                                                                     self.ids["background_b"].norm_image_size[
                                                                         1] * staticConfigurables.graphics.getfloat(
                                                                         "TitleScreen",
                                                                         "content_size_relative_to_background_b_height")
                                                                     )

        Logger.info("TitleScreen: Created content_image and background_b_image")

        self.parent.set_screen("JoinGameScreen")
