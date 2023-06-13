'''
Module to store constants for Pivotal API
Variables
    MY_PROJECTS
'''
from enum import Enum


class PivotalTrackerApiRoutes(Enum):
    '''
    A class to Enum constants for endpoints
    '''
    MY_PROJECTS = "/projects/"
    WORKSPACES = "/my/workspaces/"
    STORIES = "/stories/"
    LABELS = "labels/"
    EPICS = "epics/"


class PivotalFeatures(Enum):
    """Enum Created to manage PIVOTAL Features constants
    """
    WORKSPACE = 0
    PROJECT = 1
    STORY = 2
    LABEL = 3
    EPIC = 4


class PayloadsRoute(Enum):
    """Enum Created to manage the routes for payloads
    """
    ROUTE = "/main/pivotal_tracker/api/resources/"


class ConfigurationsRoute(Enum):
    """Enum Created to manage the routes for configurations needed
    """
    ROUTE = "/main/core/resources/"


class PivotalSearchFeature(Enum):
    """Enum Created to search Pivotal Features
    """
    WORKSPACES = "Workspaces"
    PROJECTS = "Projects"
    STORIES = "Stories"
    EPICS = "Epics"
    LABELS = "Labels"
