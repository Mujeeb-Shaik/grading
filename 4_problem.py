"""
GCD of two numbers using for loop
Example 1 :
Input 60,48
Output=12

"""

import unittest
def GCD_Loop( a, b):  
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
class TestGCD_Loop(unittest.TestCase):

    def test_01(self):
        input_nums = [60,48]
        output_num = 12

        self.assertEqual(GCD_Loop(input_nums[0],input_nums[1]), output_num)

    def test_02(self):
        input_nums = [54,24]
        output_num = 6

        self.assertEqual(GCD_Loop(input_nums[0],input_nums[1]), output_num)



if __name__ == '__main__':
    unittest.main(verbosity=2)
