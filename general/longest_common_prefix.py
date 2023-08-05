'''
14. LONGEST COMMON PREFIX
https://leetcode.com/problems/longest-common-prefix/

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        maxLength = min([len(x) for x in strs])
        for iChar in range(maxLength):
            letters = [x[iChar] for x in strs]
            letters_equal = True
            for iltr in range(len(letters)-1):
                letters_equal = letters_equal and (letters[iltr] == letters[iltr+1])
            if letters_equal:
                prefix = prefix + letters[0]        
            else:
                break
        
        return prefix

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))