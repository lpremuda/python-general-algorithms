'''
383. RANSOM NOTE
https://leetcode.com/problems/ransom-note/

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in magazine:
            if ch in ransomNote:
                # Remove the first occurence of ch from ransomNote
                ransomNote = ransomNote.replace(ch,"",1)
        
        return ransomNote == ""
        
       