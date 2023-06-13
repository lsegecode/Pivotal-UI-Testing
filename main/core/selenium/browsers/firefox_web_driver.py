"""Module to define Firefox Web Driver
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from get_gecko_driver import GetGeckoDriver


class FirefoxWebDriver:
    """Firefox web driver implementation
    """
    type_browser = None

    @staticmethod
    def initialize(**kwargs):
        """This method initialices a instance of Firefox.

        Returns:
            driver: return the webdriver for Firefox
        """

        get_driver = GetGeckoDriver()
        get_driver.install()
        firefox_options = Options()
        for key, value in kwargs.items():
            if value:
                firefox_options.add_argument(f'--{key}')
        desired_capabilities = DesiredCapabilities.FIREFOX
        desired_capabilities['acceptInsecureCerts'] = True
        FirefoxWebDriver.type_browser = webdriver.Firefox()
        return FirefoxWebDriver.type_browser
