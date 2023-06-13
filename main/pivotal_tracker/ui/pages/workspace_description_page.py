"""Module for WorkspaceDescription
"""
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class WorkspaceDescriptionPage:
    """Workspace description page
    """
    stories_nav_tag = (By.XPATH, '//a[@data-aid="navTab-stories"]')

    def __init__(self, driver):
        """Initialize with a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def get_workspace_id(self):
        """get workspace id from URL

        Return:
        -------
        id --> int
        """
        WebDriverConditions.presence_of_element_located(self.driver, self.stories_nav_tag)
        return int(self.driver.current_url.split('/')[-1])
