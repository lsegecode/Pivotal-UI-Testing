"""
Module with Pivotal API Endpoints
Class:
    EpicsPivotalEndpoints
Functions:
    get_all_my_epics(optional) --> dict
    create_epic(optional) --> dict
    get_epic(int, optional) --> dict
    update_epic(int, optional) --> dict
    delete_epic(int, optional) --> dict
"""

from main.pivotal_tracker.utils.pivotal_tracker_constants \
    import PivotalTrackerApiRoutes as PTAR
from main.core.api.http_methods_enum import HttpMethods
from main.core.api.request_manager import RequestManager


class EpicsPivotalEndpoints:
    """Endpoints for PivotalTraker API
    Functions
    ---------
        get_all_my_epics(optional) --> dict
        get all epics
        create_epic(optional) --> dict
        create an epic
        get_epic(int, optional) --> dict
        get a specific epic
        update_epic(int, optional) --> dict
        update an epic
        delete_epic(int, optional) --> dict
        delete an epic
    """
    @staticmethod
    def get_all_my_epics(fields=None):
        """
        Parameters
        ----------
            fields : dict --> optional
        Returns
        -------
            dict --> all the epics
        """
        endpoint_epic_route = PTAR.EPICS.value
        response = RequestManager.get_instance().\
            send_request(HttpMethods.GET.value,
                         endpoint_epic_route,
                         fields)
        return response

    @staticmethod
    def create_epic(project_id, fields=None):
        """
        Posts a new epic
        Args:
        project_id(int): the id of the epic to be created
        payload_dict(dict): the data to create

        Returns:
        response(object): the response object
        """
        endpoint_epic_route = f"{PTAR.MY_PROJECTS}{project_id}" \
                              f"{PTAR.EPICS.value}"
        response = RequestManager.get_instance().\
            send_request(HttpMethods.POST.value,
                         endpoint_epic_route,
                         fields)
        return response

    @staticmethod
    def get_epic(project_id, epic_id):
        """
        Basic method to get the projects of an epic

        Parameters
        ----------
        project_id : int
        epic_id : int
        id of the workspace to search fro

        Returns
        -------
        response
        request response
        """
        endpoint_epic_route = f"{PTAR.STORIES.value}" \
                              f"{project_id}/epics/{epic_id}"
        return RequestManager.get_instance().\
            send_request(HttpMethods.GET.value,
                         endpoint_epic_route)

    @staticmethod
    def update_epic(project_id, epic_id, fields=None):
        """Parameters
        ----------
        project_id : int
        epic_id : int
        fields : dict --> optional
        Return
        ------
        dict --> a specific project
        """
        endpoint_epic_route = f"{PTAR.MY_PROJECTS.value}{project_id}" \
                              f"{PTAR.STORIES.value}{epic_id}"
        response = RequestManager.get_instance().\
            send_request(HttpMethods.PUT.value,
                         endpoint_epic_route,
                         fields)
        return response

    @staticmethod
    def delete_epic(project_id, epic_id):
        """Basic method to delete an epic

        Parameters
        ----------
        project_id : int
        epic_id: int

        Returns
        -------
        response
        request response
        """
        endpoint_epic_route = f"{PTAR.MY_PROJECTS.value}{project_id}" \
                              f"{PTAR.STORIES.value}{epic_id}"
        response = RequestManager.get_instance().\
            send_request(HttpMethods.DELETE.value,
                         endpoint_epic_route)
        return response
