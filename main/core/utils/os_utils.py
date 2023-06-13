"""Module for storing methods and variables related to the operating system
that the application is running on"""
import os


def build_path_for_current_os(path):
    """
    Method to build a directory path based on the os.
    Works for Linux and Windows.

    Parameters
    ----------
    path (list): application relative path, each folder is an item.

    Returns
    -------
        (str): processed path for linux or windows
    """
    return os.path.abspath(os.sep.join(path))
