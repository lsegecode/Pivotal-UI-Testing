"""Module for stories
verifications
"""
from dataclasses import asdict
from assertpy import assert_that
from pytest_bdd import parsers, then
from main.pivotal_tracker.ui.components.stories.invalid_name_story_page import InvalidName
from main.pivotal_tracker.ui.components.stories.create_story_modal import CreateStoryModal
from main.pivotal_tracker.ui.pages.project_description_page import ProjectDescriptionPage


@then(parsers.parse("I should verify the story title"))
def step_story_verification_created(request):
    """step to verify project info details

    Args:
        request (object)    : request object of fixture
    """
    story_page = ProjectDescriptionPage(request.browser)
    story_name = story_page.get_story_name()
    expected_story = asdict(request.story_entity)
    assert_that(story_name["name"]).is_equal_to(expected_story["name"])


@then(parsers.parse('I confirm the deletion of the story \"{story_name}\"'))
def step_story_verification_deletion(story_name, request):
    """ step to verify story
    deletion
    Args:
    request(object)
    story_name(str)
    """
    project_page = ProjectDescriptionPage(request.browser)
    story_name_list = project_page.result_list_stories()
    matches = [t for t in story_name_list if story_name.lower() in t.lower()]
    assert len(matches) == 0


@then(parsers.parse('I confirm the change of the \"{story_name}\"'))
def step_story_verification_update(request):
    """ step to verify story
    update
    Args:
    request(object)
    story_name(str)
    """
    story_page = ProjectDescriptionPage(request.browser)
    story_name = story_page.get_story_name()
    expected_story = asdict(request.story_entity)
    assert_that(story_name["name"]).is_equal_to(expected_story["name"])


@then('I confirm the Story is in currentbacklog')
def step_story_verification_drop_backlog(request):
    """ step to verify story
    is in current backlog
    Args:
    request(object)
    """
    project_page = ProjectDescriptionPage(request.browser)
    story_name_list = project_page.result_list_stories()
    matches = list(story_name_list)
    assert len(matches) == 1


@then('I check the Story state is Started')
def step_story_verification_feature_started(request):
    """ step to verify story
    is started
    Args:
    request(object)
    """
    story_page = CreateStoryModal(request.browser)
    state = story_page.get_state()
    assert state == 'Started'


@then('I check an error window is displayed')
def step_story_verification_invalid_name(request):
    """ step to verify error
    window
    Args:
    story_name(str)
    """
    error_page = InvalidName(request.browser)
    header = error_page.get_header()
    assert header == 'Validation Error'
