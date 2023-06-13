"""Module for abstracting the Start page's functionality"""
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class StartPage:
    """
    A class to abstract the properties and functionality of the Start page.
    ...
    Attributes
    ----------
    login_button(tuple) : web locator tuple
    """
    login_button = (By.XPATH, "//div[@class='header__lg'] "
                              "//a[contains(@class,'header__link-signin')]")

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        """
        Function for clicking the log in button
        """
        WebDriverConditions.visibility_of(self.driver, self.login_button)
        self.driver.find_element(*self.login_button).click()
