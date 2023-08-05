'''
28. FIND THE INDEX OF THE FIRST OCCURRENCE IN A STRING
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle) and haystack[i+j] == needle[j]:
                j += 1
            if j == len(needle):
                return i
            
        return -1

s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))
print(s.strStr("mississippi", "issip"))
