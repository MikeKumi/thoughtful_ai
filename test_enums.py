"""
This module acts as unittest for the DispatchStacks enum.

Source: enums.py
Author: Michael Kumicich
Date:   January 26, 2025
"""


import unittest
from enums import DispatchStacks

class TestDispatchStacks(unittest.TestCase):
    def test_DispatchStacks_Standard(self):
        self.assertEqual(DispatchStacks.STANDARD.value, 'STANDARD')

    def test_DispatchStacks_Special(self):
        self.assertEqual(DispatchStacks.SPECIAL.value, 'SPECIAL')

    def test_DispatchStacks_Rejected(self):
        self.assertEqual(DispatchStacks.REJECTED.value, 'REJECTED')

if __name__ == "__main__":
    unittest.main()
