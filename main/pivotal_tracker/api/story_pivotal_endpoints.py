"""Module for story pivotal api
"""
from main.pivotal_tracker.utils.pivotal_tracker_constants \
    import PivotalTrackerApiRoutes as PAR
from main.core.api.http_methods_enum import HttpMethods
from main.core.api.request_manager import RequestManager


class StoryPivotalEndpoints:
    """Class to make requests to Stories Pivotal Endpoints
    """
    @staticmethod
    def get_all_my_story(fields=None):
        """Basic method to get all my stories

        Parameters
        ----------
        fields : Dict, optional
            fields to request, by default None

        Returns
        -------
        response
            request response
        """
        endpoint = PAR.STORIES.value
        return RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint,
            fields
        )

    @staticmethod
    def get_projects_stories(story_id):
        """Basic method to get the stories of an project

        Parameters
        ----------
        story_id : str
            id of the story to search fro

        Returns
        -------
        response
            request response
        """
        endpoint = f"{PAR.STORIES.value}{story_id}/projects"
        return RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint
        )

    @staticmethod
    def get_story(project_id, story_id, fields=None):
        """Basic method to get story by id

        Parameters
        ----------
        story_id : int
        project_id : int
        fields : Dict, optional
            fields to request, by default None

        Returns
        -------
        response
            request response
        """
        endpoint = f"{PAR.MY_PROJECTS.value}{project_id}" \
                   f"{PAR.STORIES.value}{story_id}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.GET.value,
            endpoint,
            fields
        )
        return response

    @staticmethod
    def update_story(project_id, story_id, fields=None):
        """
        Parameters
        ----------
            project_id : int
            story_id : int
            fields : dict --> optional
        Return
        ------
            dict --> a specific project
        """
        endpoint_story = f"{PAR.MY_PROJECTS.value}{project_id}" \
                         f"{PAR.STORIES.value}{story_id}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.PUT.value,
            endpoint_story,
            fields
        )
        return response

    @staticmethod
    def delete_story(project_id, story_id, fields=None):
        """Basic method to delete a story

        Parameters
        ----------
        story_id : int
        project_id :  int
        fields : dict
        Returns
        -------
        response
            request response
        """
        endpoint = f"{PAR.MY_PROJECTS.value}{project_id}" \
                   f"{PAR.STORIES.value}{story_id}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.DELETE.value,
            endpoint,
            fields
        )
        return response

    @staticmethod
    def create_story(project_id, fields=None):
        """Basic method to create a story

        Parameters
        ----------
        project_id : int
        fields : dict
            mandatory fields to create an story

        Returns
        -------
        response
            request response
        """
        endpoint = f"{PAR.MY_PROJECTS.value}{project_id}" \
                   f"{PAR.STORIES.value}"
        response = RequestManager.get_instance().send_request(
            HttpMethods.POST.value,
            endpoint,
            fields
        )
        return response
