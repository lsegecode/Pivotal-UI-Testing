"""
This module lets the dev create a custom logger
Classes:
    CustomLogger
Functions:
    __init__(name) -> object
    close()
Misc variables:
    handlers
"""
import logging
import logging.config
import datetime


class Logger(logging.Logger):
    """
    A class to implement the use of a customized data logger, based on the
    native logging lib.
    ...
    Attributes
    ----------
    name : str
        the name with which the logger will be identified and accessed.
    Methods
    -------
    close():
        Terminates the handlers and with that, the logger.
    """
    handlers = []

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the Logger to work
        properly.
        Parameters
        ----------
            name(str): the name with which the logger will
            be identified and accessed.
        """
        logging.Logger.__init__(self, name)
        console_handler = logging.StreamHandler()
        aux_string = \
            "./logs/" \
            f"{datetime.datetime.now().isoformat(' ', 'seconds')[:10]} " \
            ".log"
        file_handler = logging.FileHandler(aux_string)
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)
        format_str = '%(asctime)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(format_str, datefmt='%d-%m-%y %H:%M:%S')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        self.handlers = self.handlers + [console_handler, file_handler]

    def close(self):
        """
        Terminates the handlers and with that, the logger.
        """
        for handler in self.handlers:
            handler.flush()
            handler.close()
