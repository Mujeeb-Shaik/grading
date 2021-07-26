"""
??? Question with two examples ???
"""

import unittest


def factorial(num):
    """
    ??? Write what needs to be done ???
    """
    pass

# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class Testfactorial(unittest.TestCase):

    def test_01(self):
        input_num = 5
        output_num = 120

        self.assertEqual(factorial(input_num), output_num)

    def test_02(self):
        input_num = 4
        output_num = 24

        self.assertEqual(factorial(input_num), output_num)


    def test_03(self):
        input_num = 3
        output_num = 6

        self.assertEqual(factorial(input_num), output_num)


if __name__ == '__main__':
    unittest.main(verbosity=2)
