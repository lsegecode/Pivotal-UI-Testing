""" Module for stories
    actions
"""
from pytest_bdd import when, parsers
from main.core.utils.string_utils import StringUtils
from main.pivotal_tracker.ui.components.stories.create_story_modal import CreateStoryModal
from main.pivotal_tracker.entities.story import Story
from main.pivotal_tracker.ui.pages.project_dashboard_page import ProjectDashboardPage
from main.pivotal_tracker.ui.pages.project_description_page import ProjectDescriptionPage
from main.pivotal_tracker.ui.pages.story_delete_page import StoryDeletePage
from tests.utils.random_data_generator import RandomDataGenerator


@when('I create the story with random data')
def step_create_story(request):
    """step to create a story

    Args:
        request (request): request fixture object
    """
    random_data_generator = RandomDataGenerator()
    story_random_data = random_data_generator.story_generator()
    project_description_page = ProjectDescriptionPage(request.browser)
    project_description_page.click_add_story_button()
    story_info = story_random_data
    create_story_modal = CreateStoryModal(request.browser)
    request.story_entity = Story(**story_info)
    create_story_modal.create_story(request.story_entity)


@when('I click on Current/backlog panel on Left Sidebar')
def step_click_current_backlog(request):
    """step to click
    current backlog

    Args:
        request (request): request fixture object
    """
    ProjectDashboardPage(request.browser).click_on_current_backlog()


@when('I click on the Delete button')
def step_click_delete_button(request):
    """step to delete
    a story

    Args:
        request (request): request fixture object
    """
    CreateStoryModal(request.browser).click_delete_story_button()
    StoryDeletePage(request.browser).click_delete_btn()


@when('I edit the Story name')
def step_edit_story_name(request):
    """step to edit a story

    Args:
        request (request): request fixture object
    """
    random_data_generator = RandomDataGenerator()
    story_random_data = random_data_generator.story_generator()
    story_info = story_random_data
    create_story_modal = CreateStoryModal(request.browser)
    request.story_entity = Story(**story_info)
    create_story_modal.update_story_name(request.story_entity)


@when(parsers.parse('I drag and drop the \"{story_name}\" from icebox to currentbacklog'))
def step_story_drag_and_drop(story_name, request):
    """step to drag and
    drop a story

    Args:
        story_name (string):
        request (request): request fixture object
    """
    story_name_formated = StringUtils.replace_tag(story_name, request)
    story = ProjectDescriptionPage(request.browser)
    story.drag_and_drop_story(story_name_formated)


@when('I change the story type to bug')
def step_change_story_type(request):
    """step to change
    story type

    Args:
        request (request): request fixture object
    """
    creat_story_modal = CreateStoryModal(request.browser)
    creat_story_modal.change_story_stype()


@when('I change the story points')
def step_change_story_points(request):
    """step to assign
    story point

    Args:
        request (request): request fixture object
    """
    creat_story_modal = CreateStoryModal(request.browser)
    creat_story_modal.assign_story_point()


@when('I change the story state from Unstarted to Started')
def step_change_story_state(request):
    """step to change story
    state

    Args:
        request (request): request fixture object
    """
    create_story_modal = CreateStoryModal(request.browser)
    create_story_modal.start_story()


@when('I click on the add story button')
def step_click_add_story(request):
    """step to add
    story

    Args:
        request (request): request fixture object
    """
    project_page = ProjectDescriptionPage(request.browser)
    project_page.click_add_story_button()


@when('I click on the save button')
def step_click_save_button(request):
    """step to click
    save button

    Args:
        request (request): request fixture object
    """
    create_story_modal = CreateStoryModal(request.browser)
    create_story_modal.click_save_button()
