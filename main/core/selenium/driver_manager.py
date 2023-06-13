"""Module to define Web Driver Factory
"""
from main.core.selenium.browsers.chrome_web_driver import ChromeWebDriver
from main.core.selenium.browsers.firefox_web_driver import FirefoxWebDriver
from main.core.selenium.browsers.remote_web_driver import RemoteWebDriver


class DriverManager:
    """Class to define WebDriver factory
    """

    _browsers = {
        "CHROME": ChromeWebDriver,
        "FIREFOX": FirefoxWebDriver,
        "REMOTE": RemoteWebDriver,
    }

    @classmethod
    def get_driver(cls, browser="CHROME", **kwargs):
        """Method to get a specific browser driver
        Parameters
        ----------
        browser : str, optional
            type of browser, by default "CHROME"
        Returns
        -------
        object
            browser driver object
        """
        return cls._browsers[browser].initialize(**kwargs)
