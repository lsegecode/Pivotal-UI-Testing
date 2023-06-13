"""Module for pivotal ui project test verifications steps.
"""
from dataclasses import asdict
from assertpy import assert_that
from pytest_bdd import then, parsers
from main.pivotal_tracker.ui.pages.project_more_option_page\
    import ProjectMoreOptionPage
from main.logger.logger import Logger


LOGGER = Logger(name='project_verifications_ui-logger')


@then(parsers.parse("I verify that the Project information "
                    "is displayed on Project Details page"))
def step_project_verification_project_created(request):
    """step to verify project info details

    Args:
        request (object)    : request object of fixture
    """
    LOGGER.info("I verify that the Project information "
                "is displayed on Project Details page")
    expected_project = asdict(request.project_entity)
    project_more_option = ProjectMoreOptionPage(request.browser)
    project_more_option_info, error_message = project_more_option.get_project_info()
    project_more_option_info = asdict(project_more_option_info)

    if error_message is not None:
        assert_that(error_message).is_equal_to("Name can't be blank")
    else:
        for key, value in expected_project.items():
            if value != '':
                assert_that(project_more_option_info[key]).is_equal_to(value)


@then('I verify that the Project information is updated')
def step_project_verification_update(request):
    """step to verify that a project is updated

    Args:
        request (object)    : request object of fixture
    """
    LOGGER.info('I verify that the Project information is updated')
    project_more_option = ProjectMoreOptionPage(request.browser)
    project_more_option_info = project_more_option.get_project_info()
    expected_project = asdict(request.project_entity)

    for key, value in expected_project.items():
        if key != "name":
            if value is None:
                assert_that(project_more_option_info[key]).is_equal_to('')
            else:
                assert_that(project_more_option_info[key]).is_equal_to(value)
