"""Module to define Remote Web Driver
"""
import warnings
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class RemoteWebDriver:
    """Remote web driver implementation
    """
    type_browser = None

    @staticmethod
    def initialize(**kwargs):
        """This method initialices a instance of Remote Browser.

        Returns:
            driver: return the webdriver for Remote Browser
        """

        warnings.filterwarnings(action="ignore", message="unclosed",
                                category=ResourceWarning)
        browser = kwargs.get('remote_browser')
        hub_ip = kwargs.get('remote_ip')
        hub_port = kwargs.get('remote_port')
        capabilities = {}

        if browser == 'CHROME':
            capabilities = DesiredCapabilities.CHROME
        elif browser == 'FIREFOX':
            capabilities = DesiredCapabilities.FIREFOX

        return webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=f"http://{hub_ip}:{hub_port}/wd/hub")
