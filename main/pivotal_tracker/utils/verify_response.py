"""Module to verify the request response"""
from json import JSONDecodeError
import jsonschema
from assertpy import assert_that
from main.core.utils.json_reader import JsonReader


class VerifyResponse:
    """Class defined to verify the request response"""

    @staticmethod
    def verify_response_body(response, expected, request):
        """Method to verify the response body

        Parameters
        ----------
        response : response
            request response
        expected : response
            expected response
        request : object
            request fixture object
        """

        differences = ""
        try:
            if request.context["members_endpoint"]:
                response = [resp for resp in response
                            if resp["id"] == expected["id"]][0]
            if isinstance(response, list):
                for field, value in expected.items():
                    for item in response:
                        item_field = item.get(field, None)
                        assert_that(item_field).is_not_none()
                        assert_that(item_field).is_equal_to(value)

            if isinstance(response, dict):
                response_field = {}
                for field, value in expected.items():
                    keys = field.split(".")
                    for index, each_key in enumerate(keys):
                        response_field = str(response.get(
                            each_key, None) if index == 0 else
                            response_field.get(each_key, None))
                    assert_that(response_field).is_equal_to(value)
        except AssertionError:
            differences = "The following fields are not the same:\n\n"
            for field, value in expected.items():
                if expected[field] != response[field]:
                    differences += \
                        f"Expected ==> \"{field}\": \"{value}\" " \
                        f"is not equal to "
                    differences += \
                        f"Response ==> \"{field}\": " \
                        f"\"{response.get(field)}\"\n"

    @staticmethod
    def verify_status_code(response_status_code, status_code_expected):
        """Method to verify status code of the response
        Parameters
        ----------
        status_code : int
            status code value
        expected : int
            status code expected
        """
        assert_that(response_status_code).is_equal_to(status_code_expected)

    @staticmethod
    def verify_response_schema(
            response,
            json_schema,
            base_path="./main/pivotal_tracker/api/"
                      "resources/response_schemas/"):
        """Method to Verify that the response follows the expected schema

        Args:
            response (dict): response
            expected (str): name of the file in jsonschema 4.0 format
            base_path (str): default /main/pivotal/api/
            resources/response_schemas/
        """
        template = ""
        try:
            template = JsonReader.get_json(f"{base_path}{json_schema}")
        except JSONDecodeError as err:
            return False, str(err)

        try:
            jsonschema.validate(instance=response, schema=template)
            return True, "Schema successfully verified"
        except jsonschema.exceptions.ValidationError as err:
            return False, str(err)
