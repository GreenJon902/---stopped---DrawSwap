from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.button import Button


class HoverButton(Button):
    mouse_over = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        self.register_event_type("on_mouse_enter")
        self.register_event_type("on_mouse_leave")
        super(Button, self).__init__(*args, **kwargs)

        Window.bind(mouse_pos=self.on_mouse_move)

    def on_mouse_move(self, window, pos):
        if self.collide_point(*pos):
            if not self.mouse_over:
                self.dispatch("on_mouse_enter", pos, self)
        else:
            if self.mouse_over:
                self.dispatch("on_mouse_leave", pos, self)

    def on_mouse_enter(self, mouse_pos, widget):
        self.mouse_over = True

    def on_mouse_leave(self, mouse_pos, widget):
        self.mouse_over = False
