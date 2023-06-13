"""String utils for the application
"""
import re


class StringUtils:
    """Class defined to manage strings
    """
    @staticmethod
    def replace_tag(string, request):
        """Method to replace the "string" with the content inside
            "request" if it has a tag < >

        Parameters
        ----------
        string : str --> endpoint
            string value contains < and >, for instance: <Boards.id>
        request : object
            request fixture object

        Returns
        -------
        object
            content inside request with the name "string"
        """
        matches = re.findall(r"<[\w\.]*>", string)
        for match in matches:
            if match:
                feature_name, feature_property = re.search(r"[\w\.]+",
                                                           match)[0].split(".")
                feature = request.context[feature_name.lower()]
                if feature_property in feature:
                    value = str(feature[feature_property])
                else:
                    value = str(request.body[feature_property])
                string = re.sub(f"{match}", value, string)
        return string

    @staticmethod
    def replace_empty_values(value, request, module_name):
        """Method to replace the empty values with the content inside "request"

        Parameters
        ----------
        value : string
            string value contains, for instance: idBoard
        request : object
            request fixture object
        module_name: string
            module name

        Returns
        -------
        object
            content inside request with the name "value"
        """
        match = re.search(r"[\w\.]+", value)[0]
        content = re.findall("[A-Za-z][^A-Z]*", match)
        feature_name = f"{content[-1]}s".lower()
        feature_number = re.search(r"([0-9]+)$", module_name)
        if feature_number:
            feature_name += f"{feature_number[0]}"
        feature_property = "".join(content[0:-1])
        feature = request.context[feature_name]
        value = feature.get(feature_property, value)
        return value

    @staticmethod
    def convert_keys_to_snake_case(dict_table):
        """Method to convert dictionary key names to snake case

        Parameters
        ----------
        dict_table : dict
            dictionary table

        Returns
        -------
        table_converted : dict
            dictionary key names converted to snake case
        """
        table_converted = {}
        for key, value in dict_table.items():
            match = re.findall(r"[A-Z][a-z]+", key[0].upper() + key[1:])
            propert_name = "_".join([word.lower() for word in match[:-1]])
            table_converted[propert_name] = value
        return table_converted

    @staticmethod
    def change_name(payload, module_name):
        """Method to change the name of the module
            according to the number of fixture

        Parameters
        ----------
        payload : json
            json content for the payload
        module_name: string
            module name

        Returns
        -------
        dict
            payload content changed
        """
        match = re.search(r"([0-9]+)$", module_name)
        if match:
            for key, value in payload.items():
                if value.upper().startswith("AUTO"):
                    payload[key] = f"{value}_{match[0]}"
        return payload
