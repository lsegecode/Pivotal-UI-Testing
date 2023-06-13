"""Module to define Chrome Web Driver
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from chromedriver_py import binary_path


class ChromeWebDriver:
    """Chrome web driver implementation
    """
    type_browser = None

    @staticmethod
    def initialize(**kwargs):
        """This method initializes an instance of Chrome.
        Returns:
            driver: return the webdriver for Chrome"""
        chrome_options = webdriver.ChromeOptions()
        for key, value in kwargs.items():
            if value:
                chrome_options.add_argument(f'--{key}')
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities['acceptInsecureCerts'] = True
        ChromeWebDriver.type_browser = webdriver.Chrome(
            executable_path=binary_path,
            desired_capabilities=desired_capabilities,
            options=chrome_options
        )
        return ChromeWebDriver.type_browser
