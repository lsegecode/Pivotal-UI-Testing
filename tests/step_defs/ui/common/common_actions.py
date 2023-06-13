"""Module to define ui trello test steps common actions.
"""
from pytest_bdd import when, given, parsers
from main.core.utils.string_utils import StringUtils
from main.core.utils.json_reader import JsonReader
from main.pivotal_tracker.ui.pages.start_page import StartPage
from main.pivotal_tracker.ui.pages.login_page import LoginPage
from main.pivotal_tracker.ui.pages.dashboard_page import DashboardPage
from main.pivotal_tracker.ui.pages.project_description_page import ProjectDescriptionPage
from main.logger.logger import Logger
from main.pivotal_tracker.entities.project import Project
from main.pivotal_tracker.entities.workspace import Workspace
from main.pivotal_tracker.ui.components.create_workspace_modal\
    import CreateWorkspaceModal
from main.pivotal_tracker.ui.components.create_project_modal\
    import CreateProjectModal
from main.pivotal_tracker.ui.pages.workspace_description_page import WorkspaceDescriptionPage
from main.pivotal_tracker.ui.components.projects.project_header\
    import ProjectHeader
from tests.utils.random_data_generator import RandomDataGenerator


config_file = JsonReader.get_json('./configuration.json')
env_selected = config_file.get("environment", "test")
environment = JsonReader.get_json('./environment.json').get(env_selected)
USERNAME = environment.get("users")["admin"]["username"]
PASSWORD = environment.get("users")["admin"]["password"]
LOGGER = Logger(name='common_actions_ui-logger')


@given("I log in to Pivotal portal")
def step_log_in(request):
    """step to log in

    Args:
        request (request): request fixture object
    """
    LOGGER.info("I log in to Pivotal portal")
    StartPage(request.browser).click_login()
    LoginPage(request.browser).login(USERNAME, PASSWORD)


@when(parsers.parse('I create the \"{entity}\" with random data'))
def step_create_entity(entity, request):
    """step to create a entity

    Args:
        request (request): request fixture object
    """
    LOGGER.info('I create the \"{entity}\" with random data')
    random_data_generator = RandomDataGenerator()
    project_random_data = random_data_generator.project_create_generator()
    info = project_random_data
    if entity == 'project':
        create_project_modal = CreateProjectModal(request.browser)
        request.project_entity = Project(**info)
        create_project_modal.create_project(request.project_entity)
    else:
        create_workspace_modal = CreateWorkspaceModal(request.browser)
        request.workspace_entity = Workspace(**info)
        create_workspace_modal.create_workspace(request.workspace_entity)


@when(parsers.parse('I get the Id \"{entity}\" from the description page'))
def step_get_entity_id(entity, request):
    """step to get a entity id
    Args:
        entity (string): the entity Ex: project, workspace
        request (request): request fixture object
    """
    LOGGER.info('I get the Id \"{entity}\" from the description page')
    if entity == "project":
        project_description_page = ProjectDescriptionPage(request.browser)
        project_id = project_description_page.get_project_id()
        request.context["project"] = {"id": project_id}
    else:
        workspace_description_page = WorkspaceDescriptionPage(request.browser)
        workspace_id = workspace_description_page.get_workspace_id()
        request.context["workspace"] = {"id": workspace_id}


@when(parsers.parse("I click on \"{tag_name}\" tag on dashboard tabs"))
def step_clicks_tag_dashboard(request, tag_name):
    """step to click on plus button

    Args:
        tag_name (string): tag_name
        request (request): request fixture object
    """
    LOGGER.info("I click on \"{tag_name}\" tag on dashboard tabs")
    dashboard_tag = DashboardPage(request.browser)
    dashboard_tag.click_on_dashboard_tabs(tag_name)


@when(parsers.parse("I click on \"{button_name}\" button"))
def step_clicks_button_create(request, button_name):
    """step to click on button create

    Args:
        button_name (string): button_name
        request (request): request fixture object
    """
    LOGGER.info("I click on \"{button_name}\" button")
    dashboard_tag = DashboardPage(request.browser)
    dashboard_tag.click_create_option_btn(button_name)


@when('I search the project on the search bar')
def step_search_project(request):
    """step to search a project on the search bar
    on scenario outline

    Args:
        request (request): request fixture object
    """
    project_name_formatted = StringUtils.replace_tag("<Project.name>", request)
    dashboard = DashboardPage(request.browser)
    dashboard.search_on_search_bar(project_name_formatted)
    dashboard.click_on_a_project(project_name_formatted)


@when(parsers.parse('I search \"{project_name}\" on the search bar'))
def step_search_on_searchbar(project_name, request):
    """step to search a project on the search bar

    Args:
        project_name (string): project_name
        request (request): request fixture object
    """
    LOGGER.info('I search \"{project_name}\" on the search bar')
    project_name_formatted = StringUtils.replace_tag(project_name, request)
    dashboard = DashboardPage(request.browser)
    dashboard.search_on_search_bar(project_name_formatted)
    dashboard.click_on_a_project(project_name_formatted)


@when(parsers.parse('I click on the \"{entity_name}\" on \"{entity}\"'))
def step_click_on_a_entity(entity, entity_name, request):
    """step to click on a entity

    Args:
        entity (string): The name of the entity
        entity_name (string): entity_name
        request (request): request fixture object
    """
    LOGGER.info('I click on the \"{entity_name}\" on \"{entity}\"')
    if entity == 'project':
        project_name_formatted = StringUtils.replace_tag(entity_name, request)
        dashboard = DashboardPage(request.browser)
        dashboard.click_on_a_project(project_name_formatted)
    else:
        workspace_name_formatted = StringUtils.replace_tag(entity_name, request)
        dashboard = DashboardPage(request.browser)
        dashboard.click_on_a_workspace(workspace_name_formatted)


@when(parsers.parse('I click the \"{story_name}\"'))
def step_click_on_a_story(story_name, request):

    """step to click on a story

    Args:
        story_name (string): story_name
        request (request): request fixture object
    """

    LOGGER.info('I click on the \"{story_name}\"')

    story_name_formated = StringUtils.replace_tag(story_name, request)
    story = ProjectDescriptionPage(request.browser)
    story.click_on_a_story(story_name_formated)


@when(parsers.parse('I click on \"{nav_option}\" navigation tab'))
def step_see_click_on_a_nav_option(nav_option, request):
    """step to click on a nav option

    Args:
        request (request): request fixture object
        nav_option: (string): option on nav
    """
    LOGGER.info('I click on \"{nav_option}\" navigation tab')
    project_header = ProjectHeader(request.browser)
    project_header.click_on_element(nav_option)
