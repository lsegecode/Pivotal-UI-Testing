"""Workspace header component.
"""
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class ProjectHeader:
    """Workspace header component implementation.
    """
    option_selected = lambda self, option: (  # noqa: E731
        By.XPATH, f'//nav/a/span[text()="{option.lower()}"]')

    def __init__(self, driver):
        """Initializes the component using the web driver.

        Args:
            driver (object): Web driver
        """
        self.driver = driver

    def click_on_element(self, option):
        """Clicks on the element give the locator
        Parameters
        ----------
        option
            option to find the element according if it is project or workspace
        """
        WebDriverConditions.element_to_be_clickable(
            self.driver, self.option_selected(option))
        self.driver.find_element(*self.option_selected(option)).click()
