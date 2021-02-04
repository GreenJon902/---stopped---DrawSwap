import os
import pathlib
from shutil import copyfile

import AppInfo

if __name__ == "__main__":
    if not os.path.exists(AppInfo.user_data_dir):
        os.makedirs(AppInfo.user_data_dir)

    if not os.path.exists(AppInfo.user_data_file):
        copyfile(AppInfo.default_user_data_file, AppInfo.user_data_file)

    os.chdir(pathlib.Path(__file__).parent.absolute())
    os.environ["KIVY_NO_ARGS"] = "1"
    os.environ["KIVY_HOME"] = AppInfo.kivy_home_dir
    os.environ["KCFG_KIVY_LOG_NAME"] = "%y-%m-%d_%_.log"
    os.environ["KCFG_KIVY_LOG_DIR"] = AppInfo.log_dir
    os.environ["KCFG_KIVY_LOG_LEVEL"] = "info"

    from kivy.logger import Logger

    Logger.info("Base: kivy module fully loaded")


    import Graphics

    Graphics.load_kv()
    Logger.info("Base: kv_language loaded")

    Logger.info("Base: Graphics fully loaded")

    Graphics.start()

    Logger.info("Base: App has finished!")
