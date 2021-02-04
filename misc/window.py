resizable = True
_last_size = (100, 100)


def on_resize(window, width, height):
    if resizable:
        global _last_size
        _last_size = width, height

    else:
        window.size = _last_size
