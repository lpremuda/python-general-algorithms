#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 12:15:28 2022

@author: lucas.premuda
"""

import unittest

class Solution:
    def max_profit(self, prices: list[int]) -> int:
        max_prof = 0
        lowest = prices[0]
        for price_today in prices[1:]:
            if price_today <= lowest:
                lowest = price_today
            else: 
                prof_today = price_today - lowest
                max_prof = max(max_prof, prof_today)
                
        return max_prof
            
            
        

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.max_profit([7,1,5,3,6,4]), 5)
        
    def test_case_2(self):
        self.assertEqual(self.solution.max_profit([7,6,4,3,1]), 0)

        
unittest.main()