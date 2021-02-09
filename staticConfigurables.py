from configparser import ConfigParser

import AppInfo

textures = ConfigParser()
textures.read(AppInfo.texture_link_file)

settings = ConfigParser(interpolation=None)
settings.read(AppInfo.settings_file)

graphics = ConfigParser(interpolation=None)
graphics.read(AppInfo.graphics_file)
