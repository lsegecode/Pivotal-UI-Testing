""" module to Workspace entity"""
from dataclasses import dataclass
from typing import Any


@dataclass
class Story:
    """
    Project entity Class

    """
    name: Any = ""
    description: Any = ""
