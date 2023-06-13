"""
Module with Pivotal API Endpoints
Class:
    ProjectsPivotalEndpoints
Functions:
    get_all_my_projects(optional) --> dict
    get_project(int, optional) --> dict
    create_project(optional) --> dict
    update_project(int, optional) --> dict
    delete_project(int, optional) --> dict
"""
from main.pivotal_tracker.utils.pivotal_tracker_constants \
    import PivotalTrackerApiRoutes as PTAR
from main.core.api.http_methods_enum import HttpMethods
from main.core.api.request_manager import RequestManager


class ProjectsPivotalEndpoints:
    """
    Endpoints for PivotalTraker API
    Functions
    ---------
    get_all_my_projects(optional) --> dict
        get all projects
    get_project(int, optional) --> dict
        get a specific project
    create_project(optional) --> dict
        create a project
    update_project(int, optional) --> dict
        update a project
    delete_project(int, optional) --> dict
        delete a project
    """

    @staticmethod
    def get_all_my_projects(fields=None):
        """
        Parameters
        ----------
            fields : dict --> optional
        Returns
        -------
            dict --> all the projects
        """
        endpoint_project_projects_route = PTAR.MY_PROJECTS.value
        response = RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint_project_projects_route,
            fields
        )
        return response

    @staticmethod
    def get_project(project_id, fields=None):
        """
        Parameters
        ----------
            project_id : int
            fields : dict --> optional
        Return
        ------
            dict --> a specific project
        """
        endpoint_project = f"{PTAR.MY_PROJECTS.value}" \
                           f"{project_id}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint_project,
            fields
        )
        return response

    @staticmethod
    def create_project(fields=None):
        """
        Parameters
        ----------
            fields : dict --> optional
        Returns
        -------
            dict --> a specific project
        """
        endpoint_project = PTAR.MY_PROJECTS.value
        response = RequestManager.get_instance().send_request(
            HttpMethods.POST.value,
            endpoint_project,
            fields
        )
        return response

    @staticmethod
    def update_project(project_id, fields=None):
        """
        Parameters
        ----------
            project_id : int
            fields : dict --> optional
        Return
        ------
            dict --> a specific project
        """
        endpoint_project = f"{PTAR.MY_PROJECTS.value}" \
                           f"{project_id}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.PUT.value,
            endpoint_project,
            fields
        )
        return response

    @staticmethod
    def delete_project(project_id, fields=None):
        """
        Parameters
        ----------
            project_id : int
            fields : dict --> optional
        Return
        ------
            dict --> a specific project
        """
        endpoint_project = f"{PTAR.MY_PROJECTS.value}" \
                           f"{project_id}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.DELETE.value,
            endpoint_project,
            fields
        )
        return response
