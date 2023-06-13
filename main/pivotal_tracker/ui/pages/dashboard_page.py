"""Module for dashboard page"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from main.core.selenium.webdriver_conditions import WebDriverConditions


class DashboardPage:
    """
    A class for the dashboard page.

    ...

    Attributes
    ----------
    project_list(tuple) : web locator tuple
    create_project_btn(tuple) : web locator tuple
    """
    create_project_btn = (By.ID, "create-project-button")
    search_bar = (By.ID, "projects-search-bar")
    project_list = (By.CSS_SELECTOR, "a.projectTileHeader"
                                     "__projectName--active")
    workspace_list = (By.CSS_SELECTOR, "a.WorkspaceTile__name")
    workspace = lambda self, workspace: (
        By.XPATH, f'//a[@class="WorkspaceTile__name"][text()="{workspace}"]')
    tag_on_nav = lambda self, option: (  # noqa: E731
        By.XPATH, f'//span[text()="{option}"]')
    button_create = lambda self, option: (  # noqa: E731
        By.XPATH, f'//button[text()="{option}"]')
    project_link = lambda self, project_name: (  # noqa: E731
        By.CSS_SELECTOR,
        f'div.projectTileHeader__title span[data-balloon="{project_name}"]')

    def __init__(self, driver):
        """
        Function to initialize the class
        parameter
        ---------
        driver(webdriver)
        """
        self.driver = driver

    def click_on_dashboard_tabs(self, option):
        """
        Function for clicking in a dashboard tag
        """
        WebDriverConditions.visibility_of(self.driver, self.tag_on_nav(option))
        self.driver.find_element(*self.tag_on_nav(option)).click()

    def click_create_option_btn(self, option):
        """
        Function for clicking in create option button
        """
        WebDriverConditions.visibility_of(
            self.driver, self.button_create(option))
        self.driver.find_element(*self.button_create(option)).click()

    def click_on_a_project(self, project_name):
        """
        Function for clicking in a project
        """
        WebDriverConditions.element_to_be_clickable(
            self.driver, self.project_link(project_name))
        self.driver.find_element(*self.project_link(project_name)).click()

    def search_on_search_bar(self, project_name):
        """
        Function for searchin a project on search bar
        """
        WebDriverConditions.visibility_of(
            self.driver, self.search_bar)
        self.driver.find_element(*self.search_bar).click()
        self.driver.find_element(
            *self.search_bar).send_keys(project_name + Keys.RETURN)

    def result_list_projects(self):
        """
        Function to get list of projects
        Return:
        ---------
        projects_names(list)
        """
        WebDriverConditions.visibility_of(
            self.driver, self.project_list)
        links = self.driver.find_elements(*self.project_list)
        projects_names = [link.text for link in links]
        return projects_names

    def click_on_a_workspace(self, workspace_name):
        """
        Function to click on a workspace
        Parameters:
        ---------
        workspace_name
        """
        WebDriverConditions.element_to_be_clickable(
            self.driver, self.workspace(workspace_name))
        self.driver.find_element(*self.workspace(workspace_name)).click()

    def result_list_workspaces(self):
        """
        Function to get list of workspaces
        Return:
        ---------
        workspaces_names(list)
        """
        WebDriverConditions.visibility_of(
            self.driver, self.workspace_list)
        links = self.driver.find_elements(*self.workspace_list)
        workspaces_names = [link.text for link in links]
        return workspaces_names
