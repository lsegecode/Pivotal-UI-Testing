"""Module to define pivotal api common actions.
"""
from sttable import parse_str_table
from pytest_bdd import given, when, then, parsers
from main.core.utils.parse_request_body import ParseRequestBody
from main.core.api.request_manager import RequestManager
from main.core.utils.string_utils import StringUtils
from main.pivotal_tracker.utils.api_utils import ApiUtils


@given(parsers.parse("the following body parameters:\n{body}"))
def step_set_body_parameters(datatable, body, request):
    """set body parameters

    Args:
        datatable (datatable): kind of class object to interact with datatables
        body (datatable): body datatable composed by keys and values
        request (object): request fixture object
    """
    datatable.body = parse_str_table(body)
    body = ParseRequestBody.generate_data(datatable.body.rows, request)
    request.body = body


@when(parsers.parse("the \"{http_method}\" request to \"{endpoint}\" is sent"))
@then(parsers.parse("the \"{http_method}\" request to \"{endpoint}\" is sent"))
def step_do_request(http_method, endpoint, request):
    """Do request to the endpoint

    Args:
        http_method (string): http method or verb
        endpoint (string): endpoint used to interact with request manager
        request (request): request fixture object
        account (string): account which the request will do
    """
    endpoint = StringUtils.replace_tag(endpoint, request)

    response, status_code = RequestManager.get_instance().send_request(
        http_method,
        endpoint,
        request.body)
    ApiUtils.save_request_response(request, http_method,
                                   response, status_code, endpoint)
