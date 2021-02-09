import os
from configparser import ConfigParser

import AppInfo


class _textureConfigParser(ConfigParser):
    def get(self, *args, **kwargs) -> str:
        path = super(_textureConfigParser, self).get(*args, **kwargs)
        return os.path.join(AppInfo.resources_dir, path)


textures = _textureConfigParser()
textures.read(AppInfo.texture_link_file)

settings = ConfigParser(interpolation=None)
settings.read(AppInfo.settings_file)

graphics = ConfigParser(interpolation=None)
graphics.read(AppInfo.graphics_file)
