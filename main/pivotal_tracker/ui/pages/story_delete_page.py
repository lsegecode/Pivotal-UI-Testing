"""Module for DescriptionPage
"""
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class StoryDeletePage:
    """Delete Story Page
"""

    delete_button = (By.CSS_SELECTOR, 'button[data-aid="DeleteButton"]')

    def __init__(self, driver):
        """Initialize with a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver
        WebDriverConditions.visibility_of(self.driver, self.delete_button)

    def click_delete_btn(self):
        """Click delete

        Parameters
        ----------
        """
        self.driver.find_element(*self.delete_button).click()
