from configparser import ConfigParser

Config = ConfigParser()
Config.read("config.ini")

default = """
[ServerSettings]
port = 42069

[Database]
name = database.db
"""

save_folder = "DrawSwapServer"


def make_new():
    with open(save_folder, "w") as f:
        f.write(default)
