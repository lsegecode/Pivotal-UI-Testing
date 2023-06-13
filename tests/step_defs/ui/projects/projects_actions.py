"""Module to implement step actions"""
from pytest_bdd import when, parsers, then
from sttable import parse_str_table
from main.logger.logger import Logger
from main.core.utils.parse_request_body import ParseRequestBody
from main.pivotal_tracker.ui.components.create_project_modal\
    import CreateProjectModal
from main.pivotal_tracker.entities.project import Project
from main.pivotal_tracker.ui.components.projects.project_header\
    import ProjectHeader
from main.pivotal_tracker.ui.pages.project_more_option_page\
    import ProjectMoreOptionPage
from tests.utils.random_data_generator import RandomDataGenerator


LOGGER = Logger(name='project_actions_ui-logger')


@when(parsers.parse('I change the data with \"{name}\" and \"{description}\"'))
def step_update_project_data(name, description, request):
    """step to update a project

    Args:
        name (string):
        description (string):
        request (request): request fixture object
    """
    LOGGER.info('I change the data with \"{name}\" and \"{description}\"')
    if name == '(black space)':
        project_data = {'name': '         ', 'description': '           '}
    else:
        project_data = {'name': name, 'description': description}
    request.project_entity = Project(**project_data)

    project_more_page = ProjectMoreOptionPage(request.browser)
    project_more_page.update_a_project(request.project_entity)


@when(parsers.parse('I click on the \"{link}\" link'
                    ' from the \"{nav_option}\" navigation tab'))
def step_delete_project(link, nav_option, request):
    """step to delete a project

    Args:
        link (string): link name
        request (request): request fixture object
        nav_option: (string): option on nav
    """
    LOGGER.info('I click on the \"{link}\" link'
                ' from the \"{nav_option}\" navigation tab')
    project_header = ProjectHeader(request.browser)
    project_header.click_on_element(nav_option)

    project_more_page = ProjectMoreOptionPage(request.browser)
    project_more_page.delete_a_project(link)


@when(parsers.parse('I change the description with'
                    ' random data on \"{nav_option}\" navigation tab'))
def step_update_project(nav_option, request):
    """step to update a project

    Args:
        request (request): request fixture object
        nav_option: (string): option on nav
    """
    LOGGER.info('I change the description with'
                ' random data on \"{nav_option}\" navigation tab')
    project_header = ProjectHeader(request.browser)
    project_header.click_on_element(nav_option)
    random_data_generator = RandomDataGenerator()
    project_random_data = random_data_generator.project_update_generator()
    request.project_entity = Project(**project_random_data)

    project_more_page = ProjectMoreOptionPage(request.browser)
    project_more_page.update_a_project(request.project_entity)


@when('I try to create the project without a name and an account')
def step_create_a_project_without_required_data(request):
    """step to create a project without required data

    Args:
        request (request): request fixture object
    """
    LOGGER.info('I try to create the project without a name and an account')
    create_project_modal = CreateProjectModal(request.browser)
    create_project_modal.click_on_create()


@then(parsers.parse('I update the project with:\n{body}'))
def step_update_project_fields(datatable, body, request):
    """step to update project fields
    Args:
        datatable (dict): datatable object
        body: (dict): scenario outline
        request (request): request fixture object
    """
    datatable.body = parse_str_table(body)
    body = ParseRequestBody.generate_data(datatable.body.rows, request)
    project_info = body
    request.project_entity = Project(**project_info)

    project_more_page = ProjectMoreOptionPage(request.browser)
    project_more_page.update_project_fields(request.project_entity)
