"""Module where the epic actions are defined
"""
from pytest_bdd import when, parsers
from main.pivotal_tracker.ui.components.epics.create_epic import CreateEpic
from main.pivotal_tracker.ui.components.epics.delete_epic import DeleteEpic
from main.pivotal_tracker.ui.components.epics.update_epic import UpdateEpic
from main.pivotal_tracker.entities.epics import Epics  # pylint: disable=C0412

from tests.utils.random_data_generator import RandomDataGenerator


@when(parsers.parse('I create an epic with random data'))
def step_create_epic(request):
    """Step to create a project.

    Args:
        datatable (string):
        table (string): status code
        request (request): request fixture object
    """
    random_data_generator = RandomDataGenerator()
    epic_random_data = random_data_generator.epic_generator()
    epic_info = epic_random_data
    request.epic_entity = Epics(**epic_info)

    create_epic = CreateEpic(request.browser)
    create_epic.create_new_epic(request.epic_entity)


@when(parsers.parse('I delete an epic'))
def step_delete_epic(request):
    """ Step to delete an epic
    Args:
        datatable (string):
        talbe (string): status code
        request (request): request fixture object
    """
    delete_epic = DeleteEpic(request.browser)
    delete_epic.delete_epic()


@when(parsers.parse('I modify the title of an epic'))
def step_modify_epic_title(request):
    """Step to modify the title of an epic

    Args: Datatable(string)
    table(string): status code
    request: request fixture object
    """
    random_data_generator = RandomDataGenerator()
    epic_random_data = random_data_generator.epic_generator()
    epic_info = epic_random_data
    request.epic_entity = Epics(**epic_info)

    change_epic_title = UpdateEpic(request.browser)
    change_epic_title.change_epic_title(request.epic_entity)


@when(parsers.parse('I follow an epic'))
def follow_epic(request):
    """Step to follow an Epic
    Args: Datatable(string)
    table(string): status code
    request: request fixture object
    """
    update_epic = UpdateEpic(request.browser)
    update_epic.follow_the_epic()


@when(parsers.parse('I add an epic description'))
def add_epic_description(request):
    """Step to add an epic description
    Args: Datatable(string)
    table(string): status code
    request: request fixture object
    """
    random_data_generator = RandomDataGenerator()
    epic_random_data = random_data_generator.epic_generator()
    epic_info = epic_random_data
    request.epic_entity = Epics(**epic_info)

    new_description = UpdateEpic(request.browser)
    new_description.add_epic_description(request.epic_entity)
