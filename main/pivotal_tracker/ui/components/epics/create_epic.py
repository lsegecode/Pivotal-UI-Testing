"""Module for the creation of an epic
"""
from main.core.selenium.webdriver_conditions import WebDriverConditions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # noqa:F401


class CreateEpic:
    """ Class to implement the creation of an epic
"""
    epic_tag = (By.XPATH, "//span[text()='Epics']")
    add_epic_btn = (By.XPATH, "//span[text()='Add Epic']")
    epic_name_input = (By.CSS_SELECTOR, "textarea[aria-label*=story]")
    epic_save_btn = (By.XPATH, "//button[text()='Save']")
    epic_title = (By.XPATH, "//span[contains(@class, 'tracker_markup')]")
    header = (By.XPATH, "//header[contains(@data-bb, 'PanelHeader')]")

    def __init__(self, driver: Chrome):
        """Initialize the page
        Parameters
        --------------
        driver : object
            browser driver object
        """
        self.driver = driver

    def create_new_epic(self, epic):
        """This method creates new epic
        Parameters:
        ------------------------
        Epic: object to be created
            Is an entity
        """

        # wait for the elements to appear
        WebDriverConditions.visibility_of(self.driver, self.epic_tag)

        # click on the epics tag
        self.driver.find_element(*self.epic_tag).click()

        # wait for the element to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.add_epic_btn)

        # click on the "add epic" button
        self.driver.find_element(*self.add_epic_btn).click()

        # wait for the placeholder element to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.epic_save_btn)

        # complete the epic name input
        self.driver.find_element(*self.epic_name_input).send_keys(epic.name, Keys.ENTER)

    def get_epic_name(self):
        """This method creates new epic
        Parameters:
        ------------------------
        Epic: object to be created
            Is an entity
        """
        # Wait for the element to appear
        self.driver.find_element(*self.header).is_displayed()

        # get the text
        epic_name = self.driver.find_element(*self.epic_title).text
        return epic_name
