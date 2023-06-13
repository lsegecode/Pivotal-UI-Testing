"""Module to define helper methods for Pivotal API
"""
from main.pivotal_tracker.utils.pivotal_tracker_constants \
    import PivotalFeatures
from main.core.utils.string_utils import StringUtils


class ApiUtils:
    """Class to define helper methods for Pivotal API
    """
    @staticmethod
    def sort_tags_by_features(request, scenario):
        """Method to sort tags, depending on the Pivotal
         feature order, based on PivotalFeatures constant

        Parameters
        ----------
        request : object
            request fixture object
        scenario : object
            scenario object that includes tags

        Returns
        -------
        list
            list sorted
        """
        if any("fixture" in tag.split("_")[0] for tag in scenario.tags):
            fixture_tags = list(
                filter(lambda tag: tag.split("_")[-1].
                       rstrip('0123456789').upper() in
                       PivotalFeatures.__members__, scenario.tags))
            fixture_tags = sorted(
                fixture_tags, key=lambda tag: tag.split("_")[1][0])
            fixture_tags = sorted(
                fixture_tags,
                key=lambda tag: PivotalFeatures[
                    tag.split("_")[-1].
                    rstrip('0123456789').upper()].value)
            non_fixture_tags = list(
                filter(lambda tag: tag.split("_")[-1].
                       rstrip('0123456789').upper() not in
                       PivotalFeatures.__members__, scenario.tags))
            scenario_tags = non_fixture_tags + fixture_tags
        else:
            scenario_tags = list(scenario.tags)
        request.tags = scenario_tags
        return scenario_tags

    @staticmethod
    def replace_empty_payload_values(payload, request, module_name):
        """Method to replace the empty payload values
        with the content inside "request"

        Parameters
        ----------
        payload : json
            json content for the payload
        request : object
            request fixture object
        module_name : strinh
            module name

        Returns
        -------
        dict
            payload content filled
        """
        for field, value in payload.items():
            if value == "":
                payload[field] = StringUtils.\
                    replace_empty_values(field, request, module_name)
        return payload

    @staticmethod
    def save_request_response(request, http_method, response,
                              status_code, endpoint):
        """Method to store the request response and status
        code into the "request" object

        Parameters
        ----------
        request : object
            request fixture object

        http_method : string
            http method

        response : dict
            request response

        status_code : int
            status code value

        endpoint : string
            API endpoint
        """

        if "members" in endpoint:
            request.context["members"] = response[0]
            request.context["members_endpoint"] = True
        if http_method == "POST":
            request.context[f'{endpoint.split("/")[-1]}'[:-1]] = response

        request.response["body"] = response
        request.response["status_code"] = status_code
