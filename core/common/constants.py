import os
import platform


class Global(object):
    PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    CHROME_DRIVER_MAC_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("resources", "chromedriver_mac"))
    CHROME_DRIVER_LINUX_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("resources", "chromedriver_linux"))
    PLATFORM_NAME = platform.system()
    CHROME_DRIVER = CHROME_DRIVER_MAC_DIR if PLATFORM_NAME == "Darwin" else CHROME_DRIVER_LINUX_DIR
    SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("screenshots"))
