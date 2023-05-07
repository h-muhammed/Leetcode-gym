import unittest
from leet_gym.leetcode_DSA.hashmap import Summation

class HashmapTest(unittest.TestCase):
    """
    
    """
    def test_twosum():
        """
        
        """
        input_val = [[3, 2, 4], 6]
        output_val = [1, 2]
        solve = Summation()
        assert solve.twosum(input_val) == output_val