from kivy import Logger
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen

import staticConfigurables


class SplashScreen(Screen):
    video_source = staticConfigurables.textures.get("SplashScreen", "video")

    def on_kv_post(self, base_widget):
        self.ids["video_player"].opacity = 0

        Logger.info("SplashScreen: Video Started")
        self.ids["video_player"].state = "play"

        a = Animation(opacity=1, duration=staticConfigurables.graphics.getint("SplashScreen", "fade_in_length"))
        a.start(self.ids["video_player"])


    def video_finished(self, *args, **kwargs):
        Logger.info("SplashScreen: Video Finished")

        self.parent.set_screen("TitleScreen")
