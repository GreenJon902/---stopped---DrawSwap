from kivy.animation import Animation
from kivy.logger import Logger
from kivy.uix.screenmanager import Screen

import staticConfigurables


class TitleScreen(Screen):
    content_image = None

    def get_button_hover_animation(self, direction: str, this, child):
        if direction == "in":
            return Animation(
                opacity=staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_opacity"),
                size=(child.width * staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_growth"),
                      child.height * staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_growth")),
                pos=(this.x - this.width * (staticConfigurables.graphics.getfloat("TitleScreen",
                                                                                  "button_hover_growth") - 1) / 2,
                     this.y - this.height * (staticConfigurables.graphics.getfloat("TitleScreen",
                                                                                   "button_hover_growth") - 1) / 2),
                duration=staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_animation_duration"))

        elif direction == "out":
            return Animation(
                opacity=1,
                size=this.size,
                pos=this.pos,
                duration=staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_animation_duration"))

        else:
            Logger.error("TitleScreen: Get button hover animation called with incorrect direction " + str(direction))


    def play_button_pressed(self):
        self.content_image = self.ids["content"].export_as_image().texture
        self.content_image.uvpos = (0, 1)
        self.content_image.uvsize = (1, -1)
        Logger.info("TitleScreen: Content exported as image for play screen")

        self.parent.set_screen("PlayScreen")
