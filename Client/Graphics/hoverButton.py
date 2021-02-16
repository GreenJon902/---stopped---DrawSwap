from kivy.core.window import Window
from kivy.uix.button import Button


class HoverButton(Button):
    def __init__(self, *args, **kwargs):
        self.register_event_type('on_mouse_enter')
        self.register_event_type('on_mouse_leave')
        super(Button, self).__init__(*args, **kwargs)

        Window.bind(mouse_pos=self.on_mouse_move)

    def on_mouse_move(self):
        print()
