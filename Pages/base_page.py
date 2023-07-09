from typing import Any
from pathlib import Path
from selenium.common import NoSuchElementException
import Config.logger as lg
from datetime import datetime

SCREENSHOT_FILE = Path() / "Reports/screenshot"


class BaseClass:
    """
    Define BaseClass
    """

    log = lg.custom_logger()

    def __init__(self, driver):
        """
        constructor for BaseClass
        """
        self.driver = driver

    def get_element(self, locator):
        """
        method is get locator type and locator value
        :param locator: {str}
        :return:
        """
        locator_by = locator[0]  # locator Type
        locator_value = locator[1]  # locator Value
        element = self.driver.find_element(locator_by, locator_value)
        return element

    def get_text(self, text_locator: list) -> Any | None:
        """
        method is get text for particular locator type and locator value
        :param text_locator: {str}
        :return: {str | bool}
        """
        try:
            get_value = self.get_element(text_locator)
            text = get_value.text
            self.log.info("Element found with Locator:{}".format(text_locator))
        except NoSuchElementException:
            self.log.info("Element not found with Locator Type: {} and with locator value: {}".format(text_locator[0],
                                                                                                      text_locator[1]))
            self.screen_shot()
            assert False
        return text

    def clear_text(self, text_locator: list) -> Any | None:
        """
        method is clear text box in particular locator
        :param text_locator: {str}
        :return: {bool | str}
        """
        try:
            clear_box = self.get_element(text_locator)
            element = clear_box.clear()
            self.log.info("Element found with Locator:{}".format(text_locator))
        except NoSuchElementException:
            self.log.info("Element not found with Locator Type: {} and with locator value: {}".format(text_locator[0],
                                                                                                      text_locator[1]))
            self.screen_shot()
            assert False
        return element

    def send_text(self, text_locator: list, Input_text: str) -> Any | str:
        """
        Method is sent text for input text box
        :param text_locator: {str}
        :param Input_text: {str}
        :return: {bool | str}
        """
        try:
            element = self.get_element(text_locator)
            element = element.send_keys(Input_text)
            self.log.info("Element found with Locator:{}".format(text_locator))
        except NoSuchElementException:
            self.log.info("Element not found with Locator Type: {} and with locator value: {}".format(text_locator[0],
                                                                                                      text_locator[1]))
            self.screen_shot()
            assert False
        return element

    def click(self, locator: list) -> Any | None:
        """
        method is click for particle Locator value
        :param locator: {str}
        :return: {bool | str}
        """
        try:
            element = self.get_element(locator)
            element = element.click()
            self.log.info("Element found with Locator:{}".format(locator))
        except NoSuchElementException:
            self.log.info(
                "Element not found with Locator Type: {} and with locator value: {}".format(locator[0], locator[1]))
            self.screen_shot()
            assert False
        return element

    def is_visible_check(self, locator: list):
        try:
            element = self.get_element(locator)
            element = element.is_displayed()
            self.log.info("Element found with Locator:{}".format(locator))
        except NoSuchElementException:
            self.log.info(
                "Element not found with Locator Type: {} and with locator value: {}".format(locator[0], locator[1]))
            self.screen_shot()
            assert False
        return element

    def screen_shot(self):
        """
        This method will be used to take a screenshot when the test case fail.
        """
        now = datetime.now()
        filename = now.strftime("%Y_%m_%d_%H_%M_%S")
        screenshot_name = "{}/{}.png".format(str(SCREENSHOT_FILE), filename)
        self.driver.save_screenshot(screenshot_name)
