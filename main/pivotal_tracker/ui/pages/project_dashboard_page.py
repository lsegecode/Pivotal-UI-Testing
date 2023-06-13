""" Page for the project Dashboard
"""
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class ProjectDashboardPage:
    """Project more option
    """
    current_backlog = (By.CSS_SELECTOR, "ul.items li.backlog")

    def __init__(self, driver):
        """Initialize with a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def click_on_current_backlog(self):
        """
        Function for clicking in current backlog button
        """
        WebDriverConditions.element_to_be_clickable(self.driver, self.current_backlog)
        self.driver.find_element(*self.current_backlog).click()
