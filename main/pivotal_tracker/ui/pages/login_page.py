"""Module for abstracting the Login page's functionality"""
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions


class LoginPage:
    """
    A class to abstract the properties and functionality of the login page.

    ...

    Attributes
    ----------
    log(obj) : the logger instance
    username_input (tuple): web locator tuple
    password_input (tuple): web locator tuple
    login_button (tuple): web locator tuple
    next_button (tuple): web locator tuple

    Methods
    -------
    _get_login_credentials(user):
        fetches the login credentials for the user sent.
    login(user):
        executes the login flow.

    """
    signin_title = (By.CSS_SELECTOR, "div.app_signin_title")
    username_input = (By.CSS_SELECTOR, "#credentials_username")
    password_input = (By.CSS_SELECTOR,
                      ".credentials_password#credentials_password")
    login_button = (By.CSS_SELECTOR,
                    "#login_type_check_form input[type='submit']")
    next_button = (By.XPATH, "//input[@value='NEXT']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """
        This function executes the login flow on the pivotal website's login
        page.
        Parameters
        ----------
            username: (str): the username credential for logging in.
            password: (str): the password credential for logging in.
        """
        WebDriverConditions.visibility_of(self.driver, self.signin_title)

        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

        self.driver.find_element(*self.next_button).click()
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(str(password))

        self.driver.find_element(*self.login_button).click()
