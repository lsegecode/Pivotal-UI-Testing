"""Module for workspaces pivotal api
"""
from main.pivotal_tracker.utils.pivotal_tracker_constants \
    import PivotalTrackerApiRoutes
from main.core.api.http_methods_enum import HttpMethods
from main.core.api.request_manager import RequestManager


class WorkspacesPivotalEndpoints:
    """Class to make requests to Workspaces pivotal Endpoints
    """
    @staticmethod
    def get_all_my_workspaces(fields=None):
        """Basic method to get all my workspaces

        Parameters
        ----------
        fields : Dict, optional
            fields to request, by default None

        Returns
        -------
        response
            request response
        """
        endpoint_orgs_route = PivotalTrackerApiRoutes.WORKSPACES.value
        return RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint_orgs_route,
            fields
        )

    @staticmethod
    def get_workspaces_projects(workspace_id):
        """Basic method to get the projects of an workspace

        Parameters
        ----------
        workspace_id : str
            id of the workspace to search fro

        Returns
        -------
        response
            request response
        """
        endpoint = f"{PivotalTrackerApiRoutes.WORKSPACES.value}" \
                   f"{workspace_id}/projects"
        return RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint
        )

    @staticmethod
    def get_workspace(workspace_id, fields=None):
        """Basic method to get workspace by id

        Parameters
        ----------
        workspace_id : string
            Workspace ID
        fields : Dict, optional
            fields to request, by default None

        Returns
        -------
        response
            request response
        """
        endpoint_orgs_route = f"{PivotalTrackerApiRoutes.WORKSPACES.value}" \
                              f"{workspace_id}"
        return RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint_orgs_route,
            fields
        )

    @staticmethod
    def create_workspace(payload):
        """Basic method to create an workspace

        Parameters
        ----------
        payload : Dict
            mandatory fields to create an workspace

        Returns
        -------
        response
            request response
        """
        endpoint_orgs_route = f"{PivotalTrackerApiRoutes.WORKSPACES.value}"
        return RequestManager.get_instance().send_request(
            HttpMethods.POST.value,
            endpoint_orgs_route,
            payload
        )

    @staticmethod
    def update_workspace(workspace_id, payload):
        """Basic method to update an workspace

        Parameters
        ----------
        workspace_id : string
            Workspace ID
        payload : Dict, optional
            fields to request, by default None

        Returns
        -------
        response
            request response
        """
        endpoint_orgs_route = f"{PivotalTrackerApiRoutes.WORKSPACES.value}" \
                              f"{workspace_id}"
        return RequestManager.get_instance().send_request(
            HttpMethods.PUT.value,
            endpoint_orgs_route,
            payload
        )

    @staticmethod
    def delete_workspace(workspace_id):
        """Basic method to delete an workspace

        Parameters
        ----------
        workspace_id : string
            Workspace ID

        Returns
        -------
        response
            request response
        """
        endpoint_orgs_route = f"{PivotalTrackerApiRoutes.WORKSPACES.value}" \
                              f"{workspace_id}"
        return RequestManager.get_instance().send_request(
            HttpMethods.DELETE.value,
            endpoint_orgs_route
        )
