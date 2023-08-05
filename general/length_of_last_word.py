'''
58. LENGTH OF LAST WORD
https://leetcode.com/problems/length-of-last-word/

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        word_detected = False
        length = 0
        while i >= 0:
            if s[i] == " ":
                if word_detected:
                    return length 
            else:
                word_detected = True
                length += 1
            
            i -= 1
        
        return length