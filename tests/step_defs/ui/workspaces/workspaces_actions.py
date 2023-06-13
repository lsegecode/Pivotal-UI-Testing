"""Module to implement step actions"""
from pytest_bdd import when, parsers
from main.core.utils.string_utils import StringUtils
from main.logger.logger import Logger
from main.pivotal_tracker.ui.components.create_workspace_modal import CreateWorkspaceModal
from main.pivotal_tracker.entities.workspace import Workspace
from main.pivotal_tracker.ui.components.projects.project_header\
    import ProjectHeader
from main.pivotal_tracker.ui.pages.workspace_more_option_page\
    import WorkspaceMoreOptionPage
from main.pivotal_tracker.ui.pages.dashboard_page import DashboardPage


LOGGER = Logger(name='workspaces_actions_ui-logger')


@when(parsers.parse('I change the data with \"{name}\"'))
def step_update_workspace_data(name, request):
    """step to update a workspace

    Args:
        name (string): project name test
        request (request): request fixture object
    """
    LOGGER.info('I change the data with \"{name}\"')
    if name == '(black space)':
        workspace_data = {'name': '         '}
    else:
        workspace_data = {'name': name}
    request.workspace_entity = Workspace(**workspace_data)

    workspace_more_page = WorkspaceMoreOptionPage(request.browser)
    workspace_more_page.update_a_workspace(request.workspace_entity)


@when('I try to create the workspace without a name')
def step_create_a_workspace_without_required_data(request):
    """step to create a workspace without required data

    Args:
        request (request): request fixture object
    """
    LOGGER.info('I try to create the workspace without a name')
    create_workspace_modal = CreateWorkspaceModal(request.browser)
    create_workspace_modal.click_on_create()


@when(parsers.parse('I click on the \"{link}\" link'
                    ' from the \"{nav_option}\" navigation tab'))
def step_delete_workspace(link, nav_option, request):
    """step to delete a workspace

    Args:
        link (string): link name
        request (request): request fixture object
        nav_option: (string): option on nav
    """
    LOGGER.info('I click on the \"{link}\" link'
                ' from the \"{nav_option}\" navigation tab')
    project_header = ProjectHeader(request.browser)
    project_header.click_on_element(nav_option)

    workspace_more_page = WorkspaceMoreOptionPage(request.browser)
    workspace_more_page.delete_a_workspace(link)


@when('I click on the workspace')
def step_search_workspace(request):
    """step to search a workspace and click on it
        scenario outline
    Args:
        request (request): request fixture object
    """
    LOGGER.info('I click on the workspace')
    workspace_name_formatted = StringUtils.replace_tag('<Workspace.name>', request)
    dashboard = DashboardPage(request.browser)
    dashboard.click_on_a_workspace(workspace_name_formatted)
