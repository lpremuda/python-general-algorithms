'''
45. JUMP GAME II
https://leetcode.com/problems/jump-game-ii/
'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        print(nums)
        for i in range(1,len(nums)):
            nums[i] = max(i + nums[i], nums[i-1])
        
        print(nums)

        ind = 0
        num_jumps = 0

        while ind < len(nums) - 1:
            num_jumps += 1
            ind = nums[ind]
        
        return num_jumps

s = Solution()
print(s.jump([2,3,1,1,4]))