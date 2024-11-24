"""This is test module which uses pytest to test main function
"""

import pytest
from main import main

def test_main():
    """This function tests main function
    """
    assert main() == "Hello World"