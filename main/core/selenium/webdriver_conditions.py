"""Module to define WebDriver Actions
"""
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from main.core.utils.json_reader import JsonReader

config_file = JsonReader.get_json('./configuration.json')
EXPLICIT_WAIT = config_file.get("explicit_wait")


class WebDriverConditions:
    """Class to define Web driver actions
    """
    @staticmethod
    def visibility_of(driver, locator, explicit_wait=EXPLICIT_WAIT):
        """Method to wait if a specific element has visibility

        Parameters
        ----------
        driver : object
            browser driver object
        locator : tuple
            identifier of the element
        explicit_wait : int
            explicit wait time
        """
        WDW(driver, explicit_wait).until(
            EC.visibility_of(driver.find_element(*locator)))

    @staticmethod
    def element_to_be_clickable(driver, locator, explicit_wait=EXPLICIT_WAIT):
        """Method to wait if a specific element is clickable

        Parameters
        ----------
        driver : object
            browser driver object
        locator : tuple
            identifier of the element
        explicit_wait : int
            explicit wait time
        """
        WDW(driver, explicit_wait).until(
            EC.element_to_be_clickable(locator))

    @staticmethod
    def alert_is_present(driver, explicit_wait=EXPLICIT_WAIT):
        """Method to wait if a specific element is selected

        Parameters
        ----------
        driver : object
            browser driver object
        explicit_wait : int
            explicit wait time
        """
        WDW(driver, explicit_wait).until(EC.alert_is_present())

    @staticmethod
    def presence_of_element_located(driver, locator,
                                    explicit_wait=EXPLICIT_WAIT):
        """Method to wait if a specific element has
        visibility and is located
        Parameters
        ----------
        driver : object
            browser driver object
        locator : tuple
            identifier of the element
        explicit_wait : int
            explicit wait time
        """
        WDW(driver, explicit_wait).until(
            EC.presence_of_element_located(locator))

    @staticmethod
    def element_to_be_selected(driver, locator, explicit_wait=EXPLICIT_WAIT):
        """Method to wait if a specific element is selected

        Parameters
        ----------
        driver : object
            browser driver object
        locator : tuple
            identifier of the element
        explicit_wait : int
            explicit wait time
        """
        WDW(driver, explicit_wait).until(
            EC.element_to_be_selected(driver.find_element(*locator)))
