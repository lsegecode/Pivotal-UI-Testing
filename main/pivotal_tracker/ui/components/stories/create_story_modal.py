from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from main.core.selenium.webdriver_conditions import WebDriverConditions
from selenium.webdriver.common.keys import Keys


class CreateStoryModal:
    """Class to implement CreateStoryModal
    """
    add_story_btn = (By.CSS_SELECTOR, '.tn-PanelHeader__action___3zvuQp6Z:nth-child(3) .MuiButton-label')
    story_name_inp = (By.CSS_SELECTOR, 'textarea[name="story[name]"]')
    create_btn = (By.CLASS_NAME, 'autosaves button std save')
    delete_story_btn = (By.XPATH, '//button[contains(@class,"autosaves delete right_endcap hoverable")]')
    change_type_btn = (By.XPATH, '//a[@class="selection item_feature"]')
    bug_type_btn = (By.XPATH, '//a[@class="item_bug "]')
    points_btn = (By.XPATH, '//div[@class="dropdown story_estimate"]')
    two_points_btn = (By.XPATH, '//a[@class="item_2 "]')
    start_bt = (By.CSS_SELECTOR, 'button[class="state button start"]')
    save_btn = (By.CSS_SELECTOR, 'button[class="autosaves button std save"]')
    state_btn = (By.CSS_SELECTOR, 'span[data-aid="StoryState__dropdown--label"]')

    def __init__(self, driver: Chrome):
        """Initializae the create story modal using a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def create_story(self, story):
        """Method to fill story_name and create a story

        Parameters
        ----------
        story : object
        """
        WebDriverConditions.visibility_of(self.driver, self.story_name_inp)
        self.driver.find_element(*self.story_name_inp).send_keys(story.name, Keys.ENTER)

    def click_save_button(self):
        WebDriverConditions.visibility_of(self.driver, self.save_btn)
        self.driver.find_element(*self.save_btn).click()

    def click_delete_story_button(self):
        self.driver.find_element(*self.delete_story_btn).click()

    def update_story_name(self, story):
        WebDriverConditions.visibility_of(self.driver, self.story_name_inp)
        self.driver.find_element(*self.story_name_inp).clear()
        self.driver.find_element(*self.story_name_inp).send_keys(story.name + Keys.RETURN)

    def change_story_stype(self):
        self.driver.find_element(*self.change_type_btn).click()
        self.driver.find_element(*self.bug_type_btn).click()

    def assign_story_point(self):
        WebDriverConditions.visibility_of(self.driver, self.points_btn)
        self.driver.find_element(*self.points_btn).click()
        self.driver.find_element(*self.two_points_btn).click()

    def start_story(self):
        self.driver.find_element(*self.start_bt).click()

    def get_state(self):
        state = self.driver.find_element(*self.state_btn).text
        return state
