import unittest
from leetcode_DSA.hashmap import *

class HashmapTest(unittest.TestCase):
    """
    
    """
    def test_twoSum(self):
        """
        
        """
        nums = [3, 2, 4]
        target = 6

        output_val = [1, 2]
        solve = Summation()
        print(f'test is successfull!\nThe output result is: {solve.twoSum(nums, target)}')
        assert solve.twoSum(nums, target) == output_val

if __name__ == '__main__':
    HashmapTest().test_twoSum()
    unittest.main()