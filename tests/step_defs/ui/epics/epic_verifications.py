"""Module for pivotal epics tests verifications steps.
"""
from dataclasses import asdict
from pytest_bdd import then, parsers
from main.pivotal_tracker.ui.components.epics.create_epic import CreateEpic
from main.pivotal_tracker.ui.components.epics.delete_epic import DeleteEpic
from main.pivotal_tracker.ui.components.epics.update_epic import UpdateEpic


@then(parsers.parse("I should verify that the name is displayed correctly"))
def step_epic_creation_verification(request):
    """This function verify that the epic is created
    """
    epic = CreateEpic(request.browser)
    epic_name = epic.get_epic_name()
    expected_epic = asdict(request.epic_entity)
    assert epic_name == expected_epic["name"]


@then(parsers.parse("I should verify that the epic is deleted"))
def step_epic_delete_verification(request):
    """This function verify that the epic is deleted
    """
    epic = DeleteEpic(request.browser)
    elements = epic.list_of_epics()
    assert len(elements) == 0


@then(parsers.parse("I should verify that the epic title was updated"))
def step_epic_title_update(request):
    """This function verify that the epic title is updated
    """
    epic = UpdateEpic(request.browser)
    new_title = epic.verify_epic_title()
    expected_epic = asdict(request.epic_entity)
    assert new_title == expected_epic["name"]


@then(parsers.parse("I should verify that the epic is followed"))
def step_epic_followed(request):
    """This function verify that the epic is followed
    """
    epic = UpdateEpic(request.browser)
    status = epic.get_checkbox_status()
    assert status is True


@then(parsers.parse("I should verify the description can be added"))
def step_description_added(request):
    """This function verify that an epic description can be added
    """
    epic = UpdateEpic(request.browser)
    description = epic.get_description()
    expected_description = asdict(request.epic_entity)
    assert description == expected_description["name"]
