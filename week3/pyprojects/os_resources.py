"""Assignment week3:
    os_resources.py should have one class:
    OsResources
    This class should have three functions:
    def get_cpu(cls)
    def get_free_mem_perc(cls)
    def get_free_mem_mb(cls)
"""
import psutil

class OsResources:
    """ OS Resources class
    """

    @classmethod
    def get_cpu(cls):
        """this function gets cpu usage percantage for interval 1 and returns the value in perc.
        Returns:
            [int] -- cpu usage percentage
        """
        return psutil.cpu_percent(interval=1)

    @classmethod
    def get_free_mem_mb(cls):
        """this function gets the free memory in pc and returns the value in MB
        Returns:
            [int] -- [description]
        """
        mem_free = psutil.virtual_memory()[4] / 1024 / 1024 # conv to MB
        return mem_free

    @classmethod
    def get_free_mem_perc(cls):
        """this function gets the free memory and returns the value
        Returns:
            [int] -- free memory in percentage
        """
        return psutil.virtual_memory()[2]
