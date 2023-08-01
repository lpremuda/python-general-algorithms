'''
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idxsZero = []
        i = 0

        while i < len(nums):
            el = nums[i]
            if el == 0:
                idxsZero.append(i)
                i += 1
            else:
                # If idxsZero is not null, we need to swap with 
                if idxsZero:
                    iSwap = idxsZero.pop(0)
                    nums[iSwap] = el
                    nums[i] = 0
                    idxsZero.append(i)
                i += 1

        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])