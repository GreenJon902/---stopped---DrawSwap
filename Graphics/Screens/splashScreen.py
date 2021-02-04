import random

from kivy.logger import Logger
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

from staticConfigurables import settings


class SplashScreen(Screen):
    def on_size(self, *args):
        if settings.getboolean("debug", "graphics") or settings.getboolean("debug", "all"):
            def walk(widget):
                for child in widget.children:
                    walk(child)

                if widget.__class__ == Image:
                    with widget.canvas:
                        widget.canvas.clear()

                        col = random.random(), random.random(), random.random()
                        Color(rgb=col)
                        Logger.debug("graphics: SplashScreen image random and size - " +
                                     str([col, widget.pos, widget.size]))

                        Rectangle(pos=widget.pos, size=widget.size)

            for child in self.children:
                walk(child)
