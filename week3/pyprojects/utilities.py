""" Assignment week 3:
    utilities.py should have one class:

    Utilities

    This class should have three functions:

    def parse_arguments(cls)
    def write_json(cls, data)
    def ensure_dir(cls, directory)
"""
import os
import argparse
import json
import time

class Utilities:
    """Utility class
    """

    @classmethod
    def parse_arguments(cls):
        """this function parses the users input and returns the dict with data
        Returns:
            [dict] -- user input
        """
        parser = argparse.ArgumentParser(
            description="Get the sys usage and output the result to file and optionally to stdout."
        )

        parser.add_argument(
            "--no-memory",
            action="store_true",
            help="do not fetch, store or output memory data"
        )

        parser.add_argument(
            "--no-cpu",
            action="store_true",
            help="do not fetch, store or output CPU data"
        )

        parser.add_argument(
            "--stdout",
            action="store_true",
            help="output data to stdout"
        )

        args = parser.parse_args()
        return args

    @classmethod
    def write_json(cls, data):
        """this function writes passed data to json file in ouput directiory
        Arguments:
            data {dict} -- data to be written to json file
        """

        #generate filename
        file_name = str(int(time.time())) + '.json'
        file_dir = './output/'
        file_path = file_dir + file_name

        #store file
        cls.ensure_dir(file_dir)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def ensure_dir(cls, directory):
        """this function checks if folder already exists, if not it creates one
        Arguments:
            directory {string} -- directory path
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
