"""class to parse body
"""
from main.core.utils.string_utils import StringUtils


class ParseRequestBody:
    """Class defined to parse the request body
    """
    @staticmethod
    def generate_data(body, request, action="send"):
        """Method to generate body
        Parameters
        ----------
        body : datatable
            body datatable composed by keys and values
        request : object
            request fixture object
        action : string, optional
            if "action" is "send" every Boolean value like: True,
            False will be parse as a string Boolean
            if "action" is "receive" every string Boolean will be parse
            as a Boolean, by default "send"
        Returns
        -------
        Dict
            Dictionary body
        """
        data = {}
        if body is not None:
            for row in body:
                value = StringUtils.replace_tag(row["value"], request)
                if action == "send":
                    data[str(row["key"])] = ParseRequestBody.\
                        parse_to_send(value)
                elif action == "receive":
                    data[str(row["key"])] = ParseRequestBody.\
                        parse_to_receive(value)
        return data

    @staticmethod
    def parse_to_send(value):
        """Method to send parse body
        Parameters
        ----------
        value : string
            string boolean like "True", "False"
        Returns
        -------
        string
            parse string
        """
        parsed_params = {"True": "true", "False": "false", "None": "none"}
        return parsed_params.get(value)\
            if value.capitalize() in parsed_params else value

    @staticmethod
    def parse_to_receive(value):
        """Method to receive parse body
        Parameters
        ----------
        value : string
            string boolean like "True", "False"
        Returns
        -------
        Boolean
            parse boolean
        """
        parsed_params = {"True": True, "False": False, "None": None}
        return parsed_params.get(value) if value.capitalize() \
            in parsed_params else value
