from kivy.app import App
from kivy.core.window import Window

from Graphics.drawSwapScreenManager import DrawSwapScreenManager

from Graphics.Screens.splashScreen import SplashScreen
from Graphics.Screens.titleScreen import TitleScreen
from misc import window


class DrawSwap(App):
    def build(self):
        Window.bind(on_resize=window.on_resize)
        window.on_resize(None, Window.width, Window.height)

        return DrawSwapScreenManager()
