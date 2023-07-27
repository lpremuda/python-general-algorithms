'''
1. TWO SUM
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

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