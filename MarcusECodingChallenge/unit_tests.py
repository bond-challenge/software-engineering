"""
Title: Unit Testing
Author: Marcus Eberhardt
Status: Active
Type: Unit tests
Created On: 2021-06-03
Last Modified By:
Last Modified On:
Modifications:


"""

# [START imports]
import moving_average
from moving_average import get_moving_average
import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
import sys, os.path, re
from datetime import datetime
from datetime import date
from datetime import timedelta
import datedelta
import time

# Set variables


class TestTestMethods(unittest.TestCase):


    def test(self):
        get_moving_average()
        error_report(Exception("test"))



if __name__ == '__main__':
    unittest.main()
