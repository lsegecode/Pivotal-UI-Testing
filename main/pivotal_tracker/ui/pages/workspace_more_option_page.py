"""Module for WorkspaceMoreOptionsPage
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from main.core.selenium.webdriver_conditions import WebDriverConditions
from main.pivotal_tracker.entities.workspace import Workspace
from main.logger.logger import Logger


LOGGER = Logger(name='workspace_more_option_page')


class WorkspaceMoreOptionPage:
    """Workspace more option
    """
    workspace_name_input = (By.ID, 'workspace_name')
    delete_link = (By.ID, 'delete_link')
    save_button = (By.CSS_SELECTOR, 'input[type="submit"]')
    confirm_delete = (By.ID, 'confirm_delete')
    error_message = (By.CSS_SELECTOR, 'span.error_above_or_below')

    def __init__(self, driver):
        """Initialize with a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def get_workspace_info(self):
        """Method to get workspace info
        """
        WebDriverConditions.presence_of_element_located(self.driver, self.workspace_name_input)

        workspace_name_text = self.driver.find_element(
            *self.workspace_name_input).get_attribute('value')
        workspace_info = {
            "name": workspace_name_text
        }
        workspace_entity = Workspace(**workspace_info)

        try:
            error_message = self.driver.find_element(*self.error_message)
            error_message = error_message.text
        except NoSuchElementException:
            LOGGER.debug("Exception: %s", NoSuchElementException)
            error_message = None
        return workspace_entity, error_message

    def delete_a_workspace(self, link):
        """Method to delete a workspace
        Args:
        link (str) : link option
        """

        self.driver.execute_script(f'document.getElementById('
                                   f'"{link.lower()}_link").focus();')
        WebDriverConditions.visibility_of(self.driver, self.delete_link)
        self.driver.find_element(*self.delete_link).click()
        WebDriverConditions.visibility_of(self.driver, self.confirm_delete)
        self.driver.find_element(*self.confirm_delete).click()

    def update_a_workspace(self, workspace):
        """Method to update a workspace
        Args:
        workspace (str) : workspace name
        """
        workspace_name = self.driver.find_element(
            *self.workspace_name_input)
        workspace_name.clear()
        workspace_name.send_keys(workspace.name)
        self.driver.find_element(*self.save_button).click()
