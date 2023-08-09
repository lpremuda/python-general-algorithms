'''
125. VALID PALINDROME
https://leetcode.com/problems/valid-palindrome/
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers, one at the start of the string and one at the beginning
        i = 0
        j = len(s) - 1
        while i <= j:
            # If character is not an alphanumeric, move the i pointer forward
            if not s[i].isalpha() and not s[i].isdigit():
                i += 1
            # If character is not an alphanumeric, move the j pointer backward
            elif not s[j].isalpha() and not s[j].isdigit():
                j -= 1
            else:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
        
        return True

s = Solution()
print(s.isPalindrome("race a car"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))