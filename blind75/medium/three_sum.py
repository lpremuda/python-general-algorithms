#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 21:56:23 2022

@author: lucas.premuda
"""

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # Continue the for loop if the current a equals the last value in nums
            if i > 0 and nums[i-1] == a:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    
                    # Continue to increment l if it equals the last value in nums
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        return res