"""
Prime number program 
Example 1:
Input=2
Output=True

Example 2:
Input=5
Output=True

Example 3:
Input=9
Output=False
"""

import unittest

def prime(n):
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
class Testprime(unittest.TestCase):

    def test_01(self):
        input_num = 2
        output_num = True

        self.assertEqual(prime(input_num), output_num)

    def test_02(self):
        input_num = 5
        output_num = True

        self.assertEqual(prime(input_num), output_num)


    def test_03(self):
        input_num = 9
        output_num = False

        self.assertEqual(prime(input_num), output_num)



if __name__ == '__main__':
    unittest.main(verbosity=2)
