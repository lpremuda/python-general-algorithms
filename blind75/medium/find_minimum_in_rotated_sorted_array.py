# -*- coding: utf-8 -*-

import unittest
import math

class Solution:
    def max_subArray(self, nums: list[int]) -> int:
        max_sum = -math.inf
        
        # Temporary sum used for the for loop
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum < nums[i]:
                curr_sum = nums[i]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum
                
        
class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.max_subArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        
    def test_case_2(self):
        self.assertEqual(self.solution.max_subArray([5,4,-1,7,8]), 23)
        
    def test_case_3(self):
        self.assertEqual(self.solution.max_subArray([-1]), -1)
        
    def test_case_4(self):
        self.assertEqual(self.solution.max_subArray([-2, 1]), 1)

        
unittest.main()