import unittest
from package_dispatcher import sort, _is_bulky_package

class TestPackageDispatcher(unittest.TestCase):
    def test_sort_invalid_inputs(self):
        self.assertRaises(ValueError, sort, 5, 5, None, 5)
        self.assertRaises(ValueError, sort, 5, -5, 5, 5)
        self.assertRaises(ValueError, sort, 0, 5, 5, 5)
        self.assertRaises(ValueError, sort, 5, 5, 5, '5')

    def test_sort_valid_inputs(self):
        standard = sort(5, 5, 5, 5)
        self.assertEqual(standard, 'STANDARD')

        special1 = sort(5, 5, 5, 20)
        special2 = sort(150, 150, 150, 19)
        self.assertEqual(special1, 'SPECIAL')
        self.assertEqual(special2, 'SPECIAL')

        rejected = sort(150, 150, 150, 20)
        self.assertEqual(rejected, 'REJECTED')

    def test_is_bulky_package(self):
        bulky1 = _is_bulky_package(width=160, height=10, length=10)
        bulky2 = _is_bulky_package(width=10, height=160, length=10)
        bulky3 = _is_bulky_package(width=10, height=10, length=160)
        bulky4 = _is_bulky_package(width=100, height=100, length=100)
        bulky5 = _is_bulky_package(width=160, height=10, length=10)
        
        self.assertTrue(bulky1)
        self.assertTrue(bulky2)
        self.assertTrue(bulky3)
        self.assertTrue(bulky4)
        self.assertTrue(bulky5)

        notBulky = _is_bulky_package(width=99, height=99, length=99)
        self.assertFalse

if __name__ == "__main__":
    unittest.main()
