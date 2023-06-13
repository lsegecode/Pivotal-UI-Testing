"""Module for DescriptionPage
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from main.core.selenium.webdriver_conditions import WebDriverConditions


class ProjectDescriptionPage:
    """Project more option
    """
    current_backlog = (By.XPATH, '//span[text()="Current/backlog"]')
    add_story_btn = (By.CLASS_NAME, 'jss9')
    storyn = (By.CSS_SELECTOR, 'span[class="tracker_markup"]')
    story = lambda self, story_name: (By.XPATH, f"//span[@class='tracker_markup'][contains(.,'{story_name}')]")  # noqa:E501 pylint: disable=C0301
    destiny = (By.XPATH, "//div[contains(@data-iteration-type,'current')]")
    story_list = (By.CLASS_NAME, 'StoryPreviewItem__clickToExpand')

    def __init__(self, driver):
        """Initialize with a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver
        WebDriverConditions.visibility_of(self.driver, self.add_story_btn)

    def click_add_story_button(self):
        """Click add story

        Parameters
        ----------
        """
        self.driver.find_element(*self.add_story_btn).click()

    def click_on_a_story(self, story_name):
        """Click story

        Parameters
        ----------
        story_name : str
            story_name
        """
        WebDriverConditions.visibility_of(self.driver, self.story(story_name))
        self.driver.find_element(*self.story(story_name)).click()

    def drag_and_drop_story(self, story_name):
        """Drag and drop story

        Parameters
        ----------
        story_name : str
            story_name
        """

        story = self.driver.find_element(*self.story(story_name))
        action_chain = ActionChains(self.driver)
        action_chain.move_to_element(story).click_and_hold().perform()
        destiny = self.driver.find_element(*self.destiny)
        action_chain = ActionChains(self.driver)
        action_chain.move_to_element(destiny).perform()
        action_chain.release().perform()

    def get_story_name(self):
        """Get story name

        Parameters
        ----------
        """
        name_text = self.driver.find_element(*self.storyn).text
        return {"name": name_text}

    def result_list_stories(self):
        """List stories

        Parameters
        ----------
        """
        spans = self.driver.find_elements(*self.story_list)
        story_names = [link.text for link in spans]
        return story_names

    def get_project_id(self):
        """get project id from URL

        Return:
        -------
        id --> int
        """
        WebDriverConditions.presence_of_element_located(self.driver, self.current_backlog)
        return int(self.driver.current_url.split('/')[-1])
