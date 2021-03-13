from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen

import staticConfigurables
from Graphics.screenWhichIncludesHoverButton import ScreenWhichIncludesHoverButton


class JoinGameScreen(Screen, ScreenWhichIncludesHoverButton):
    background_cd_width = NumericProperty()

    def on_enter(self, *args):
        self.background_cd_width = self.ids["background_c"].width
        a = Animation(background_cd_width=0, duration=staticConfigurables.graphics.getfloat("JoinGameScreen",
                                                                                            "page_turn_speed"))
        a.bind(on_complete=self.hide_background_cd)
        a.start(self)

    def on_background_cd_width(self, _, width):
        self.ids["background_c"].width = width
        self.ids["background_d"].width = width

    def hide_background_cd(self, *args, **kwargs):
        self.ids["background_c"].opacity = 0
        self.ids["background_d"].opacity = 0

