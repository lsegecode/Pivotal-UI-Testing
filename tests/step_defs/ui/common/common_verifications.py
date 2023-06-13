"""Module for pivotal ui common test verifications steps.
"""
from pytest_bdd import then, parsers
from main.pivotal_tracker.ui.pages.dashboard_page import DashboardPage
from main.pivotal_tracker.ui.components.create_project_modal\
    import CreateProjectModal
from main.pivotal_tracker.ui.components.create_workspace_modal\
    import CreateWorkspaceModal
from main.logger.logger import Logger


LOGGER = Logger(name='project_verifications_ui-logger')


@then(parsers.parse('I confirm the deletion of the \"{entity}\" with name \"{entity_name}\"'))
def step_entity_verification_deletion(entity, entity_name, request):
    """step to verify a element is deleted

    Args:
        entity(string): feature Ex: project, workspace
        entity_name(string): project or workspace name
        request (object)    : request object of fixture
    """
    LOGGER.info('I confirm the deletion of the \"{entity}\" with name \"{entity_name}\"')
    dashboard_page = DashboardPage(request.browser)
    if entity == 'project':
        project_name_list = dashboard_page.result_list_projects()
        matches = [t for t in project_name_list
                   if entity_name.lower() in t.lower()]
        assert len(matches) == 0
    else:
        workspaces_name_list = dashboard_page.result_list_workspaces()
        matches = [t for t in workspaces_name_list
                   if entity_name.lower() in t.lower()]
        assert len(matches) == 0


@then(parsers.parse('I verify the error message '
                    '\"{error_message}\" is displayed on \"{entity}\"'))
def step_verification_error_messages(error_message, entity, request):
    """step to verify errors messages

    Args:
        error_message(str)  : error message sentence
        request (object)    : request object of fixture
    """
    LOGGER.info('I verify the error message \"{error_message}\" is displayed')
    if entity == 'projects':
        create_project_modal = CreateProjectModal(request.browser)
        error_messages = create_project_modal.error_messages()
    else:
        create_workspace_modal = CreateWorkspaceModal(request.browser)
        error_messages = create_workspace_modal.error_messages()
    assert error_message in error_messages
