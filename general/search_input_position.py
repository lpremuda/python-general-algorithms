'''
35. SEARCH INSERT POSITION
https://leetcode.com/problems/search-insert-position/

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

import math

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1            
            else:
                r = mid - 1
        
        return l

s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1], 0))
print(s.searchInsert([1,3,5], 4))
print(s.searchInsert([2,7,8,9,10], 9))
