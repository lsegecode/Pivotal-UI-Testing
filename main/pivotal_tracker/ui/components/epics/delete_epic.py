"""Module to delete an epic
"""
from main.core.selenium.webdriver_conditions import WebDriverConditions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


class DeleteEpic:
    """Class to implement the deletion of an existing epic

    """
    header = (By.XPATH, "//header[contains(@data-bb, 'PanelHeader')]")
    epic_header = (By.XPATH, '//header[contains(@data-aid,"EpicPreview")]')
    delete_button = (By.XPATH, '//button[@title="Delete this epic"]')
    delete_button_modal = (By.XPATH, '//button[contains(@data-aid,"Delete")]')
    epics_list = (By.XPATH, '//div[contains(@class,"epic model item")]')

    def __init__(self, driver: Chrome):
        """Initialize the page
        Parameters
        --------------
        driver : object
            browser driver object
        """
        self.driver = driver

    def delete_epic(self):
        # wait for the header to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.epic_header)

        # Click on the header so the epic appears
        self.driver.find_element(*self.epic_header).click()

        # wait for the delete button to appear
        WebDriverConditions.visibility_of(self.driver, self.delete_button)

        # click on the delete button
        self.driver.find_element(*self.delete_button).click()

        # wait for the modal to appear
        WebDriverConditions.visibility_of(self.driver, self.delete_button_modal)
        #time.sleep(1)

        # click on the modal button
        self.driver.find_element(*self.delete_button_modal).click()

    def list_of_epics(self):
        """This function returns a list of elements that match
        """
        self.driver.find_element(*self.header).is_displayed()
        elements = self.driver.find_elements(*self.epics_list)
        return elements
