from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class InvalidName:
    """Class to implement CreateProjectModal
    """
    header = (By.CSS_SELECTOR, 'div[data-aid="AlertDialog__title"]')

    def __init__(self, driver: Chrome):
        """Initializae the Boards header using a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def get_header(self):
        text_header = self.driver.find_element(*self.header).text
        return text_header
