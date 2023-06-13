""" module to Project entity"""
from dataclasses import dataclass
from typing import Any


@dataclass
class Project:
    """
    Project entity Class
    """
    name: Any = ""
    description: Any = ""
    enable_tasks: Any = ""
    public: Any = ""
    week_start_day: Any = ""
    start_date: Any = ""
    time_zone: Any = ""
    iteration_length: Any = ""
    point_scale: Any = ""
    initial_velocity: Any = ""
    velocity_averaged_over: Any = ""
    number_of_done_iterations_to_show: Any = ""
    automatic_planning: Any = ""
    enable_incoming_emails: Any = ""
