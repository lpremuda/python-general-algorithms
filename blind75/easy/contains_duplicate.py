#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 12:32:19 2022

@author: lucas.premuda
"""

import unittest

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        mem = set()
        for num in nums:
            if num in mem:
                return True
            else:
                mem.add(num)
        return False
        

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertTrue(self.solution.contains_duplicate([1,2,3,1]))
        
    def test_case_2(self):
        self.assertFalse(self.solution.contains_duplicate([1,2,3,4]))
        
    def test_case_3(self):
        self.assertTrue(self.solution.contains_duplicate([1,1,1,3,3,4,3,2,4,2]))

        
unittest.main()