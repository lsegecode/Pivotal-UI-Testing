"""Module to define pivotal api common steps
"""
from sttable import parse_str_table
from pytest_bdd import then, parsers
from main.pivotal_tracker.utils.verify_response import VerifyResponse
from main.core.utils.parse_request_body import ParseRequestBody


@then(parsers.parse("the response status code should"
                    " be {status_code_expected:d}"))
def step_verify_response_code(status_code_expected, request):
    """verify response code

    Args:
        status_code_expected (int): status code
        request (object): request fixture object
    """
    response_status_code = request.response["status_code"]
    VerifyResponse.verify_status_code(response_status_code,
                                      status_code_expected)


@then(parsers.parse("the response body should be"
                    " verified with:\n{table}"))
def step_verify_response_payload(datatable, table, request):
    """verify response payload

    Args:
        datatable (datatable): kind of class object to interact with datatables
        table (datatable): body datatable composed by keys and values
        request (object): request fixture object
    """

    datatable.table = parse_str_table(table)
    template = ParseRequestBody.generate_data(datatable.table.rows,
                                              request, "receive")
    response = request.response["body"]
    VerifyResponse.verify_response_body(response, template, request)
