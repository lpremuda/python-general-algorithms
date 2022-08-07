# -*- coding: utf-8 -*-

import unittest

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        mem = {}        
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in mem:
                return [mem[other_num], i]
            else:
                mem[num] = i
        
        
class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertListEqual(self.solution.two_sum([2, 7, 11, 15], 9), [0, 1])
        
    def test_case_2(self):
        self.assertListEqual(self.solution.two_sum([3, 2, 4], 6), [1, 2])

        
unittest.main()