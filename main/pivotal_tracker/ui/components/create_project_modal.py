"""Module for CreateProjectModal
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class CreateProjectModal:
    """Class to implement CreateProjectModal
    """
    project_name_inp = (By.CSS_SELECTOR,
                        'label.tc-project-name__label'
                        ' input[name="project_name"]')
    account_select_list = (By.XPATH, '//div[text()="Select an account"]')
    create_btn = (By.CLASS_NAME, 'pvXpn__Button--positive')
    account_name_select = (By.CLASS_NAME,
                           'tc-account-selector__option-account-name')
    project_privacy_checkbox = (By.CSS_SELECTOR,
                                'div.tc-project-type-chooser '
                                'input[value="public"]')
    error_message_list = (By.CSS_SELECTOR,
                          'div.tc-form__input--error-message span')

    def __init__(self, driver: Chrome):
        """Initialize the creation project modal using a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def create_project(self, project):
        """Method to fill project_name and create project

        Parameters
        ----------
        project : object
            project entity
        """
        WebDriverConditions.visibility_of(self.driver, self.project_name_inp)
        self.driver.find_element(
            *self.project_name_inp).send_keys(project.name)
        WebDriverConditions.element_to_be_clickable(
            self.driver, self.account_select_list)
        self.driver.find_element(*self.account_select_list).click()

        WebDriverConditions.visibility_of(
            self.driver, self.account_name_select)
        self.driver.find_element(*self.account_name_select).click()

        WebDriverConditions.element_to_be_clickable(
            self.driver, self.project_privacy_checkbox)
        self.driver.find_element(*self.project_privacy_checkbox).click()

        self.click_on_create()

    def click_on_create(self):
        self.driver.find_element(*self.create_btn).click()

    def error_messages(self):
        """Method to collect error messages
        Return:
        error_messages(list): list of error messages sentences
        """
        self.click_on_create()

        WebDriverConditions.visibility_of(self.driver, self.error_message_list)
        spans = self.driver.find_elements(*self.error_message_list)

        error_messages = [span.text for span in spans]
        return error_messages
