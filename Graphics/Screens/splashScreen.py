import random

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen


class SplashScreen(Screen):
    def on_size(self, *args):
        def walk(widget):
            for child in widget.children:
                walk(child)

            if widget.__class__ == Image:
                with widget.canvas:
                    widget.canvas.clear()

                    col = random.random(), random.random(), random.random()
                    Color(rgb=col)
                    print(col, widget.pos, widget.size)

                    Rectangle(pos=widget.pos, size=widget.size)

        for child in self.children:
            walk(child)
