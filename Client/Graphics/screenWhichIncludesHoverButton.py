from kivy.animation import Animation
from kivy.logger import Logger

import staticConfigurables


class ScreenWhichIncludesHoverButton:
    def button_hover_animation(self, direction: str, this, child):
        if direction == "in":
            a = Animation(
                opacity=staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_opacity"),
                size=(child.width * staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_growth"),
                      child.height * staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_growth")),
                pos=(this.x - this.width * (staticConfigurables.graphics.getfloat("TitleScreen",
                                                                                  "button_hover_growth") - 1) / 2,
                     this.y - this.height * (staticConfigurables.graphics.getfloat("TitleScreen",
                                                                                   "button_hover_growth") - 1) / 2),
                duration=staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_animation_duration"))

        elif direction == "out":
            a = Animation(
                opacity=1,
                size=this.size,
                pos=this.pos,
                duration=staticConfigurables.graphics.getfloat("TitleScreen", "button_hover_animation_duration"))

        else:
            Logger.error("TitleScreen: Get button hover animation called with incorrect direction " + str(direction))
            return

        Animation.stop_all(child)
        a.start(child)
