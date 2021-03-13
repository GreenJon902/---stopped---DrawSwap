from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen

import staticConfigurables


class JoinGameScreen(Screen):
    background_c_width = NumericProperty()

    def on_enter(self, *args):
        self.background_c_width = self.ids["background_c"].width
        a = Animation(background_c_width=0, duration=staticConfigurables.graphics.getfloat("JoinGameScreen",
                                                                                           "page_turn_speed"))
        a.start(self)

    def on_background_c_width(self, _, width):
        self.ids["background_c"].width = width
