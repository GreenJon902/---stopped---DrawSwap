import AppInfo

resizable: bool = True
_last_size: [int] = int(AppInfo.default_size[0]), int(AppInfo.default_size[1])


def on_resize(window, width, height):
    if resizable:
        global _last_size
        _last_size = width, height

    else:
        window.size = _last_size
