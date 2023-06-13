"""Module for pivotal ui project test verifications steps.
"""
from dataclasses import asdict
from assertpy import assert_that
from pytest_bdd import then, parsers
from main.pivotal_tracker.ui.pages.workspace_more_option_page\
    import WorkspaceMoreOptionPage
from main.logger.logger import Logger


LOGGER = Logger(name='workspace_verifications_ui-logger')


@then(parsers.parse("I verify that the Workspace information "
                    "is displayed on Workspace Details page"))
def step_workspace_verification_workspace_created(request):
    """step to verify project info details

    Args:
        request (object)    : request object of fixture
    """
    LOGGER.info("I verify that the Workspace information "
                "is displayed on Workspace Details page")
    expected_workspace = asdict(request.workspace_entity)
    workspace_more_option = WorkspaceMoreOptionPage(request.browser)
    workspace_more_option_info, error_message = workspace_more_option.get_workspace_info()
    workspace_more_option_info = asdict(workspace_more_option_info)

    if error_message is not None:
        assert_that(error_message).is_equal_to("Name can't be blank")
    else:
        for key, value in expected_workspace.items():
            if value != '':
                assert_that(workspace_more_option_info[key]).is_equal_to(value)
