from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen

import staticConfigurables
from Graphics.screenWhichIncludesHoverButton import ScreenWhichIncludesHoverButton


class JoinGameScreen(Screen, ScreenWhichIncludesHoverButton):
    background_c_width = NumericProperty()

    def on_enter(self, *args):
        self.background_c_width = self.ids["background_c"].width
        a = Animation(background_c_width=0, duration=staticConfigurables.graphics.getfloat("JoinGameScreen",
                                                                                           "page_turn_speed"))
        a.bind(on_complete=self.hide_background_c)
        a.start(self)

    def on_background_c_width(self, _, width):
        self.ids["background_c"].width = width

    def hide_background_c(self, *args, **kwargs):
        self.ids["background_c"].opacity = 0

