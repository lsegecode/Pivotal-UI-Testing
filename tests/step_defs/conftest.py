"""This module contains shared fixtures, steps, and hooks.
"""
import datetime
import warnings
import pytest
from main.logger.logger import Logger
from main.core.api.http_methods_enum import HttpMethods
from main.pivotal_tracker.utils.pivotal_tracker_constants \
    import PayloadsRoute
from main.pivotal_tracker.utils.api_utils import ApiUtils
from main.pivotal_tracker.entities.project import Project
from main.pivotal_tracker.entities.workspace import Workspace
from main.core.utils.json_reader import JsonReader
from main.core.api.request_manager import RequestManager
from main.core.selenium.driver_manager import DriverManager as DM
from main.core.selenium.browsers_enum import Browsers
from tests.utils.random_data_generator import RandomDataGenerator as RDG


config_file = JsonReader.get_json('./configuration.json')
env_selected = config_file.get("environment", "develop")
TYPE_BROWSER = config_file.get("browser")
BROWSER_CONFIGS = config_file.get("remote_config") \
    if TYPE_BROWSER == "REMOTE" else config_file.get("browser_options")
environment = JsonReader.get_json('./environment.json').get(env_selected)
IMPLICIT_WAIT = config_file.get("implicit_wait")
URL = environment.get("ui-url")
USERNAME = environment.get("users")["admin"]["username"]
PASSWORD = environment.get("users")["admin"]["password"]

LOGGER = Logger(name='conftest-logger')


def pytest_bdd_before_scenario(request, scenario, feature):
    """ pytest bdd before scenario

    Parameters
    ----------
        request (object): request object of fixture
        feature (object): feature object of pytest bdd
        scenario (object): scenario object of pytest bdd
    """
    LOGGER.info('=============STARTED SCENARIO: %s', scenario.name)

    request.context = {
        "members_endpoint": False
    }
    request.tags = []
    request.body = {}
    request.response = {}
    scenario_tags = ApiUtils.sort_tags_by_features(request, scenario)
    request.tags += list(feature.tags)
    for tag in scenario_tags:
        if "fixture_create" in tag:
            LOGGER.info('PRE-CONDITION: TAG: %s', tag)
            module_name = tag.split('_')[-1].rstrip('0123456789')
            random_data = RDG()
            random_data = random_data.project_create_generator()
            if module_name == 'project':
                request.project_entity = Project(**random_data)
            elif module_name == 'workspace':
                request.workspace_entity = Workspace(**random_data)
            payload = random_data
            LOGGER.debug('Payload: %s', payload)
            if module_name == "workspace":
                path_endpoint = f"/my/{module_name}s"
            elif module_name == "epic":
                project_id = request.context["project"]["id"]
                path_endpoint = f"/projects/{project_id}/{module_name}s"
            elif module_name == "label":
                project_id = request.context["project"]["id"]
                path_endpoint = f"/projects/{project_id}/{module_name}s"
            elif module_name == "story":
                project_id = request.context["project"]["id"]
                path_endpoint = f"/projects/{project_id}/stories"
            else:
                path_endpoint = f"/{module_name}s"
            response, _ = RequestManager.get_instance().send_request(
                HttpMethods.POST.value,
                path_endpoint,
                payload
            )
            request.context[f"{tag.split('_')[-1]}"] = response
        elif "fake_create" in tag:
            module_name = tag.split('_')[-1].rstrip('0123456789')
            payload = JsonReader.get_json(
                f".{PayloadsRoute.ROUTE.value}"
                f"payload_{module_name}_creation_fake.json")
            request.context[f"{tag.split('_')[-1]}"] = payload

    if any(tag == "ui" for tag in scenario_tags):
        LOGGER.info(f'INITIALIZING "{Browsers[TYPE_BROWSER].value}" BROWSER')  # pylint: disable=W1203
        warnings.filterwarnings(action="ignore", category=DeprecationWarning)
        request.browser = DM.get_driver(Browsers[TYPE_BROWSER].value,
                                        **BROWSER_CONFIGS)
        request.browser.maximize_window()
        request.browser.get(URL)
        request.browser.implicitly_wait(IMPLICIT_WAIT)


def pytest_bdd_step_error(scenario, exception):
    """ pytest bdd step error

    Args:
        multiple args related with pytest bdd
    """
    LOGGER.exception('On %s exception: %s', scenario, exception)


def pytest_bdd_after_scenario(request, scenario):
    """ pytest bdd after scenario

    Args:
        request (object): request object of fixture
        scenario (object): scenario object of pytest bdd
    """
    scenario_tags = request.tags
    scenario_report = request.node.__scenario_report__.serialize()
    status = any(bool(scenario_report['steps'][step]['failed'])
                 for step in range(len(scenario_report['steps'])))
    status = 'FAILED' if status else 'SUCCESS'
    if status == 'FAILED' and any(tag == "ui" for tag in scenario_tags):
        tag_name = [tag for tag in scenario.tags if tag.startswith("tc_")][0]
        LOGGER.info('SCENARIO: %s FAILED', tag_name)
        time_now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        request.browser.save_screenshot(
            f'./reports/screenshots/scenario'
            f'_{tag_name}_{time_now}.png')

    if any(tag == "ui" for tag in scenario_tags):
        # Implement log_out
        request.browser.quit()

    for tag in scenario_tags:
        if "fixture_delete" in tag:
            LOGGER.info('POST-CONDITION: TAG: %s', tag)
            module_name = tag.split('_')[-1].rstrip('0123456789')
            element_id = request.context[f"{module_name}"]["id"]
            if module_name == "workspace":
                path_endpoint = f"/my/{module_name}s/{element_id}"
            else:
                path_endpoint = f"/{module_name}s/{element_id}"
            RequestManager.get_instance().send_request(
                HttpMethods.DELETE.value,
                path_endpoint)
    LOGGER.info('=============FINISHED SCENARIO: %s', scenario.name)


@pytest.fixture()
def datatable():
    """fixture to support implementation of datatables

    Returns:
        DataTable
    """
    return DataTable()


class DataTable:
    """Datatable Class to manage table elements
    """

    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        """
        __repr__
        """
        return self.__str__()
