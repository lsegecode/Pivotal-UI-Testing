"""Module for the creation of an epic
"""
from main.core.selenium.webdriver_conditions import WebDriverConditions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UpdateEpic:
    """Class to implement the update of an epic
    """
    epic_header = (By.XPATH, '//header[contains(@data-aid,"EpicPreview")]')
    epic_title = (By.XPATH, '//textarea[contains(@data-aid,"name")]')
    title_of_epic = (By.XPATH, '//span[contains(@class, "tracker_markup")]')
    follow_checkbox = (By.XPATH, '//input[contains(@aria-label,"follow")]')
    epic_description_box = (By.XPATH, '//div[contains(@class,"DescriptionShow")]')
    epic_description_textarea = (By.XPATH, '//textarea[contains(@placeholder,"Add a description")]')
    add_description_btn = (By.XPATH, '//button[@data-aid="save"]')
    description_added = (By.XPATH, '//div[contains(@class,"DescriptionShow")]/span/p')

    def __init__(self, driver: Chrome):
        """Initialize the page
        Parameters
        --------------
        driver : object
            browser driver object
        """
        self.driver = driver

    def change_epic_title(self, epic):
        """This method updates an epic title
        Parameters:
        ------------------------
        Epic: new title
            Is an entity
        """

        # wait for the header to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.epic_header)

        # Click on the header so the epic appears
        self.driver.find_element(*self.epic_header).click()

        # wait for the header to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.epic_title)

        # click on the title name
        self.driver.find_element(*self.epic_title).click()

        # clean the placeholder element
        self.driver.find_element(*self.epic_title).clear()

        # complete the epic name input
        self.driver.find_element(*self.epic_title).send_keys(epic.name, Keys.ENTER)

    def follow_the_epic(self):
        """This method clicks on the follow this epic checkbox
        """
        # wait for the header to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.epic_header)

        # Click on the header so the epic appears
        self.driver.find_element(*self.epic_header).click()

        # wait for the checkbox to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.follow_checkbox)

        # Click on the follow this epic checkbox
        self.driver.find_element(*self.follow_checkbox).click()

    def add_epic_description(self, epic):
        """This method adds the description to the Epic
        """
        # wait for the header to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.epic_header)

        # Click on the header so the epic appears
        self.driver.find_element(*self.epic_header).click()

        # wait for the description placeholder to appear
        WebDriverConditions.element_to_be_clickable(self.driver, self.epic_description_box)

        # Click on the epic description box
        self.driver.find_element(*self.epic_description_box).click()

        # Add a text in to the description
        self.driver.find_element(*self.epic_description_textarea).send_keys(epic.name)

        # Click on the "Add description" button
        self.driver.find_element(*self.add_description_btn).click()

    def verify_epic_title(self):
        # Wait for element to appear
        self.driver.find_element(*self.title_of_epic).is_displayed()

        # Get title
        epic_name = self.driver.find_element(*self.title_of_epic).text
        return epic_name

    def get_description(self):
        # Wait for element to appear
        self.driver.find_element(*self.description_added).is_displayed()

        # Get the text
        description = self.driver.find_element(*self.description_added).text
        return description

    def get_checkbox_status(self):
        # Wait for the element to appear
        self.driver.find_element(*self.follow_checkbox).is_displayed()

        # Get checkbox status
        status = self.driver.find_element(*self.follow_checkbox).is_selected()
        return status
