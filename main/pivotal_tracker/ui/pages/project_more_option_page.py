"""Module for WorkspaceDetails
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from main.core.selenium.webdriver_conditions import WebDriverConditions
from main.pivotal_tracker.entities.project import Project
from main.logger.logger import Logger


LOGGER = Logger(name='project_more_option_page')


class ProjectMoreOptionPage:
    """Project more option
    """
    project_name_input = (By.ID, 'project_name')
    project_desc_input = (By.ID, 'project_description')
    delete_link = (By.ID, 'delete_link')
    save_button = (By.CSS_SELECTOR, 'input[type="submit"]')
    confirm_delete = (By.ID, 'confirm_delete')
    enable_tasks_check = (By.ID, 'project_enable_tasks')
    public_check = (By.ID, 'project_public')
    week_start_day_select = (By.ID, 'project_week_start_day')
    start_date_calendar = (By.ID, 'project_start_date')
    iteration_length_select = (By.ID, 'project_iteration_length')
    initial_velocity_input = (By.ID, 'project_initial_velocity')
    number_of_done_iterations_to_show_input = (
        By.ID, 'project_number_of_done_iterations_to_show')
    automatic_planning_check = (By.ID, 'project_automatic_planning')
    enable_incoming_emails_check = (By.ID, 'project_enable_incoming_emails')
    show_story_priority_check = (By.ID, 'project_show_story_priority')
    hide_emails_from_collaborators_check = (
        By.ID, 'project_hide_emails_from_collaborators')
    time_zone_selected = (
        By.XPATH, '//select[@id="project_time_zone"]'
                  '/option[@selected="selected"]')
    point_scale_selected = (
        By.XPATH, '//select[@id="project_point_scale"]'
                  '/option[@selected="selected"]')
    velocity_scheme_selected = (
        By.XPATH, '//select[@id="project_velocity_scheme"]'
                  '/option[@selected="selected"]')

    time_zone_select_option = lambda self, option: (
        By.XPATH, f'//select[@id="project_time_zone"]'
                  f'/option[text()="{option}"]')
    point_scale_select_option = lambda self, option: (
        By.XPATH, f'//select[@id="project_point_scale"]'
                  f'/option[text()="{option}"]')
    velocity_scheme_select_option = lambda self, option: (
        By.XPATH, f'//select[@id="project_velocity_scheme"]'
                  f'/option[text()="{option}"]')

    error_message_span = (By.CSS_SELECTOR, 'span.error_above_or_below')

    def __init__(self, driver):
        """Initialize with a driver

        Parameters
        ----------
        driver : object
            browser driver object
        """
        self.driver = driver

    def get_project_info(self):
        """Method to get project info
        """
        WebDriverConditions.presence_of_element_located(self.driver, self.project_name_input)
        project_name_text = self.driver.find_element(
            *self.project_name_input).get_attribute('value')
        project_description_text = self.driver.find_element(
            *self.project_desc_input).get_attribute('value')
        enable_tasks_check_bool = self.driver.find_element(
            *self.enable_tasks_check).get_attribute('checked')
        enable_tasks_check_bool = 'true'\
            if enable_tasks_check_bool else 'false'
        public_check_bool = self.driver.find_element(
            *self.public_check).get_attribute('checked')
        public_check_bool = 'true' if public_check_bool else 'false'
        week_start_day_select_text = self.driver.find_element(
            *self.week_start_day_select).get_attribute('value')
        start_date_calendar_text = self.driver.find_element(
            *self.start_date_calendar).get_attribute('value')

        if start_date_calendar_text != "":
            start_date_calendar_text = start_date_calendar_text.split("-")
            start_date_calendar_text = start_date_calendar_text[1]\
                + '-' + start_date_calendar_text[2]\
                + '-' + start_date_calendar_text[0]

        time_zone_select_option_text = self.driver.find_element(
            *self.time_zone_selected).text
        iteration_length_text = self.driver.find_element(
            *self.iteration_length_select).get_attribute('value')
        point_scale_select_option_text = self.driver.find_element(
            *self.point_scale_selected).text
        velocity_scheme_text = self.driver.find_element(
            *self.velocity_scheme_selected).text
        initial_velocity_text = self.driver.find_element(
            *self.initial_velocity_input).get_attribute('value')
        number_of_done_iterations_to_show_text = self.driver.find_element(
            *self.number_of_done_iterations_to_show_input).\
            get_attribute('value')
        automatic_planning_check_bool = self.driver.find_element(
            *self.automatic_planning_check).get_attribute('checked')
        automatic_planning_check_bool = 'true'\
            if automatic_planning_check_bool else 'false'
        enable_incoming_emails_check_bool = self.driver.find_element(
            *self.enable_incoming_emails_check).get_attribute('checked')
        enable_incoming_emails_check_bool = 'true'\
            if enable_incoming_emails_check_bool else 'false'
        project_info = {
            "name": project_name_text,
            "description": project_description_text,
            "enable_tasks": enable_tasks_check_bool,
            "public": public_check_bool,
            "week_start_day": week_start_day_select_text,
            "start_date": start_date_calendar_text,
            "time_zone": time_zone_select_option_text,
            "iteration_length": iteration_length_text,
            "point_scale": point_scale_select_option_text,
            "initial_velocity": initial_velocity_text,
            "velocity_averaged_over": velocity_scheme_text,
            "number_of_done_iterations_to_show":
                number_of_done_iterations_to_show_text,
            "automatic_planning": automatic_planning_check_bool,
            "enable_incoming_emails": enable_incoming_emails_check_bool
        }

        project_entity = Project(**project_info)
        try:
            error_message = self.driver.find_element(*self.error_message_span)
            error_message = error_message.text
        except NoSuchElementException:
            LOGGER.debug("Exception: %s", NoSuchElementException)
            error_message = None
        return project_entity, error_message

    def delete_a_project(self, link):
        """Method to delete a project
        """
        WebDriverConditions.visibility_of(self.driver, self.delete_link)
        self.driver.execute_script(f'document.getElementById('
                                   f'"{link.lower()}_link").focus();')

        self.driver.find_element(*self.delete_link).click()
        WebDriverConditions.visibility_of(self.driver, self.confirm_delete)
        self.driver.find_element(*self.confirm_delete).click()

    def update_a_project(self, project):
        """Method to update a project
        """
        WebDriverConditions.visibility_of(self.driver, self.project_name_input)

        project_name_input = self.driver.find_element(
            *self.project_name_input)

        project_name_input.clear()
        project_name_input.send_keys(project.name)

        WebDriverConditions.visibility_of(self.driver, self.project_desc_input)

        project_desc_input = self.driver.find_element(
            *self.project_desc_input)
        project_desc_input.send_keys(project.description)

        self.driver.find_element(*self.save_button).click()

        WebDriverConditions.alert_is_present(self.driver)
        self.driver.switch_to.alert.accept()

    def evaluate_checkbox(self, locator, project_attribute):
        """Method to evaluate the checkbox
            Ex: if value sended is false and the checkbox is checked
            it is clicked
        """
        checked = self.driver.find_element(
            *locator).get_attribute("checked")
        if checked == 'true' and project_attribute == "false":
            WebDriverConditions.element_to_be_clickable(
                self.driver, locator)
            self.driver.find_element(*locator).click()
        if checked is None and project_attribute == "true":
            WebDriverConditions.\
                element_to_be_clickable(self.driver, locator)
            self.driver.find_element(*locator).click()

    def update_project_fields(self, project):
        """Method to update fields of a project
        """
        self.driver.find_element(
            *self.project_name_input).clear()
        self.driver.find_element(
            *self.project_name_input).send_keys(project.name)
        self.driver.find_element(
            *self.project_desc_input).clear()
        self.driver.find_element(
            *self.project_desc_input).send_keys(project.description)

        self.evaluate_checkbox(self.enable_tasks_check, project.enable_tasks)
        self.evaluate_checkbox(self.public_check, project.public)

        self.driver.find_element(
            *self.week_start_day_select).send_keys(project.week_start_day)
        self.driver.find_element(
            *self.start_date_calendar).clear()
        self.driver.find_element(
            *self.start_date_calendar).send_keys(project.start_date)
        self.driver.find_element(
            *self.time_zone_select_option(project.time_zone)).click()
        self.driver.find_element(
            *self.iteration_length_select).send_keys(project.iteration_length)
        self.driver.find_element(
            *self.point_scale_select_option(project.point_scale)).click()
        self.driver.find_element(
            *self.initial_velocity_input).clear()
        self.driver.find_element(
            *self.initial_velocity_input).send_keys(
            project.initial_velocity)
        self.driver.find_element(
            *self.velocity_scheme_select_option(
                project.velocity_averaged_over)).click()
        self.driver.find_element(
            *self.number_of_done_iterations_to_show_input).clear()
        self.driver.find_element(
            *self.number_of_done_iterations_to_show_input)\
            .send_keys(project.number_of_done_iterations_to_show)

        self.driver.execute_script(
            'document.getElementById('
            '"project_enable_incoming_emails").focus();')

        self.evaluate_checkbox(
            self.enable_incoming_emails_check, project.enable_incoming_emails)
        self.evaluate_checkbox(self.automatic_planning_check,
                               project.automatic_planning)

        self.driver.find_element(*self.save_button).click()
        WebDriverConditions.alert_is_present(self.driver)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.alert.accept()
