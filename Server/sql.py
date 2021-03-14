import os
import sqlite3

import config
from config import Config


def make_new():
    conn = sqlite3.connect(os.path.join(config.save_folder, Config.get("Database", "name")))
    c = conn.cursor()
