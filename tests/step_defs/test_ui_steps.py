# flake8: noqa
# pylint: skip-file
"""Module to import all pivotal ui test steps.
"""
from pytest_bdd import scenarios
from tests.step_defs.ui.common.common_actions import *
from tests.step_defs.ui.common.common_verifications import *
from tests.step_defs.ui.projects.projects_actions import *
from tests.step_defs.ui.projects.projects_verifications import *
from tests.step_defs.ui.stories.stories_actions import *
from tests.step_defs.ui.stories.stories_verifications import *
from tests.step_defs.ui.epics.epic_actions import *
from tests.step_defs.ui.epics.epic_verifications import *
from tests.step_defs.ui.workspaces.workspaces_verifications import *
from tests.step_defs.ui.workspaces.workspaces_actions import *


scenarios("../features/ui/")
