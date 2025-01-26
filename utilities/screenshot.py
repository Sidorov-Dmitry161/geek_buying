import os
from datetime import datetime


class UtilityMethods:
    @staticmethod
    def take_screenshot(driver, file_name="screenshot"):
        # Path to the folder for screenshots
        screenshots_dir = "screen"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Generated file name with current date and time
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_file_name = os.path.join(screenshots_dir, f"{file_name}_{timestamp}.png")

        # save screenshots
        driver.save_screenshot(full_file_name)
        return full_file_name
