from configparser import ConfigParser

import AppInfo

textures = ConfigParser()
textures.read(AppInfo.texture_link_file)

settings = ConfigParser(interpolation=None)
settings.read(AppInfo.settings_file)
