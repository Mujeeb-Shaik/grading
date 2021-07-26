"""
sum of first n odd numbers
Exmple 1:
input=3
output=9
Example 2:
input=7
output=49"""

import unittest


def sum_of_odd_numbers(n):
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
class Testsum_of_odd_numbers(unittest.TestCase):

    def test_01(self):
        input_num = 7
        output_num = 49

        self.assertEqual(sum_of_odd_numbers(input_num), output_num)

    def test_02(self):
        input_num = 3
        output_num = 9

        self.assertEqual(sum_of_odd_numbers(input_num), output_num)



if __name__ == '__main__':
    unittest.main(verbosity=2)
