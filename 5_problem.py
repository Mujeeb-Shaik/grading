"""
LCM of two numbers
example 1:

example 2:

"""

import unittest


def lcm(x,y):
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
class Testlcm(unittest.TestCase):

    def test_01(self):
        input_nums = [4, 6]
        output_nums = 12

        self.assertEqual(lcm(input_nums[0],input_nums[1]), output_nums)

    def test_02(self):
        input_nums = [12, 15]
        output_nums = 60

        self.assertEqual(lcm(input_nums[0],input_nums[1]), output_nums)



if __name__ == '__main__':
    unittest.main(verbosity=2)
