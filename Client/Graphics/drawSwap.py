from kivy.app import App
from kivy.core.window import Window

from misc import window

from Graphics.drawSwapScreenManager import DrawSwapScreenManager


class DrawSwap(App):
    def build(self):
        Window.bind(on_resize=window.on_resize)
        window.on_resize(None, Window.width, Window.height)

        return DrawSwapScreenManager()
