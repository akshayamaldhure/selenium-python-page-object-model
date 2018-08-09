import os

import lemoncheesecake.api as lcc

from core.common.constants import Global


def capture_screenshot(driver, target_path=os.path.join(Global.SCREENSHOTS_DIR, "screenshot.png")):
    with lcc.prepare_attachment(filename=target_path, description="Click here to view the screenshot") as filename:
        driver.save_screenshot(filename=filename)


def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            print("Deleting file {}".format(file_path))
            os.remove(file_path)
        else:
            print("File {} does not exist for deletion.".format(file_path))
    except OSError:
        print("Error deleting file {}!".format(file_path))
