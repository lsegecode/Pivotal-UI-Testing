# flake8: noqa
# pylint: skip-file
"""Module to import all pivotal api test steps.
"""
from pytest_bdd import scenarios
from tests.step_defs.api.common.common_actions import *
from tests.step_defs.api.common.common_verifications import *

scenarios("../features/api/")
