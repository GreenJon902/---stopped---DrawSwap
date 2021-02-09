from kivy.animation import Animation
from kivy.uix.screenmanager import Screen

import staticConfigurables


class SplashScreen(Screen):
    video_source = staticConfigurables.textures.get("SplashScreen", "video")

    def on_kv_post(self, *args, **kwargs):
        self.ids["video_player"].opacity = 0

        a = Animation(opacity=1, duration=staticConfigurables.graphics.getint("SplashScreen", "fade_in_length"))
        a.bind(on_complete=self.start_video)
        a.start(self.ids["video_player"])

    def start_video(self, *args, **kwargs):
        self.ids["video_player"].state = "play"
