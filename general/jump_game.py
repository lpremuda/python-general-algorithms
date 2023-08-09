'''
55. JUMP GAME
https://leetcode.com/problems/jump-game/
'''

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            else:
                reachable = max(reachable, i + nums[i])
        
        return True
