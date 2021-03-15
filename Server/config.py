import os
from configparser import ConfigParser

dev_mode = False

save_folder = "DrawSwapServer"
log_folder = os.path.join(save_folder, "Logs")

Config = ConfigParser()
Config.read(os.path.join(save_folder, "config.ini"))

default = """
[ServerSettings]
port = 42069
"""


default_db_login = """
[Login]
host=
user=
password=
database=
"""




def make_new(dev_mode):
    with open(os.path.join(save_folder, "config.ini"), "w") as f:
        f.write(default)

    Config.read(os.path.join(save_folder, "config.ini"))
