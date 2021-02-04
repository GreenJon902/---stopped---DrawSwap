from kivy.uix.screenmanager import Screen


class SplashScreen(Screen):
    def on_pre_enter(self, *args, **kwargs):
        super(SplashScreen, self).on_pre_enter(*args, **kwargs)
