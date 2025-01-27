"""
This module contains the DispatchStacks enum, which is used to avoid unexpected errors when using the stacks. 

Test:   test_enums.py
Author: Michael Kumicich
Date:   January 26, 2025
"""


from enum import Enum

class DispatchStacks(str, Enum):
    STANDARD = 'STANDARD'
    SPECIAL = 'SPECIAL'
    REJECTED = 'REJECTED'
