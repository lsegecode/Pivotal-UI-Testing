'''
Module with Pivotal API Endpoints
Class:
    LabelsPivotalEndpoints
Functions:
    get_all_my_labels(optional) --> dict
    get_label(int, optional) --> dict
    create_label(optional) --> dict
    update_label(int, optional) --> dict
    delete_label(int, optional) --> dict
'''
from main.pivotal_tracker.utils.pivotal_tracker_constants \
    import PivotalTrackerApiRoutes as PTAR
from main.core.api.http_methods_enum import HttpMethods
from main.core.api.request_manager import RequestManager


class LabelsPivotalEndpoints:
    '''
    Endpoints for PivotalTraker API
    Functions
    ---------
    get_all_my_labels(optional) --> dict
        get all labels
    get_label(int, optional) --> dict
        get a specific label
    create_label(optional) --> dict
        create a label
    update_label(int, optional) --> dict
        update a label
    delete_label(int, optional) --> dict
        delete a label
    '''

    @staticmethod
    def create_a_label(project_id, fields=None):
        """
        Posts a new label
        Args:
            project_id(int): the id of the project to be created
            payload_dict(dict): the data to create

        Returns:
            response(object): the response object
        """
        endpoint_label_route = f"{PTAR.MY_PROJECTS}{project_id}" \
                               f"{PTAR.LABELS.value}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.POST.value,
            endpoint_label_route,
            fields
        )
        return response

    @staticmethod
    def get_a_label(project_id, label_id, fields=None):
        """
        Posts a new label
        Args:
            project_id(int): the id of the project to be created
            payload_dict(dict): the data to create

        Returns:
            response(object): the response object
        """
        endpoint_label_route = f"{PTAR.MY_PROJECTS}{project_id}" \
                               f"{PTAR.LABELS.value}{label_id}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint_label_route,
            fields
        )
        return response
