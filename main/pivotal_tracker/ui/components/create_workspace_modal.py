"""Module for CreateProjectModal
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class CreateWorkspaceModal:
    """Class to implement CreateWorkspaceModal
    """

    workspace_name_input = (By.CSS_SELECTOR, 'input.tc-form__input')
    create_button = (By.XPATH, '//button[@data-aid="FormModal__submit"]')
    error_message = (By.CSS_SELECTOR,
                     'div.tc-form__input--error-message span')

    def __init__(self, driver: Chrome):
        """Initialize the creation workspace modal using a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def create_workspace(self, workspace):
        """Method to fill workspace_name and create a workspace

        Parameters
        ----------
        project : object
            workspace entity
        """
        WebDriverConditions.visibility_of(self.driver, self.workspace_name_input)

        self.driver.find_element(
            *self.workspace_name_input).send_keys(workspace.name)

        self.click_on_create()

    def click_on_create(self):
        self.driver.find_element(*self.create_button).click()

    def error_messages(self):
        """Method to collect error messages
        Return:
        -------
        error_message(list): list of error messages sentences

        """
        self.click_on_create()

        WebDriverConditions.visibility_of(self.driver, self.error_message)
        span = self.driver.find_element(*self.error_message)

        error_message = span.text
        return [error_message]
