'''
Module to enum Http Methods
Variables
    GET
    POST
    PUT
    DELETE
    PATCH
    OPTIONS
'''
from enum import Enum


class HttpMethods(Enum):
    '''
    A class to enum Http Methods
    '''
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
