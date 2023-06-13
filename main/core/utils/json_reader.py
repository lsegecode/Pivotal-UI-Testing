'''
Module to read and convert JSON files to dict
class:
    JsonReader
Functions:
    get_json(str) --> dict
'''
import json


class JsonReader:
    """JsonReader Implementation
    """
    @staticmethod
    def get_json(path):
        """Method to get configuration from a json file

        Parameters
        ----------
        config_file : json
            Json configuration file

        Returns
        -------
        Dict
            Configuration dictionary
        """
        with open(path, encoding='utf-8') as json_file:
            try:
                configuration = json.load(json_file)
            except json.JSONDecodeError as err:
                raise err
        return configuration

    def __str__(self):
        pass
