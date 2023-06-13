""" module to Workspace entity"""
from dataclasses import dataclass
from typing import Any


@dataclass
class Workspace:
    """
    Workspace entity Class

    """
    name: Any = ""
    description: Any = ""
