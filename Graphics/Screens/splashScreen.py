from kivy.uix.screenmanager import Screen

from misc import window


class SplashScreen(Screen):
    def on_pre_enter(self, *args, **kwargs):
        super(SplashScreen, self).on_pre_enter(*args, **kwargs)

        window.resizable = False
