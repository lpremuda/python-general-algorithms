'''
20. VALID PARENTHESES
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        # Initialize empty list
        open_paren = []
        
        for el in s:
            if not open_paren:
                if el in map.keys():
                    # Append open parentheses
                    open_paren.append(el)
                else:
                    # Return false because list is empty and trying to add a closing parentheses
                    return False
            else:
                if el in map.keys():
                    open_paren.append(el)
                else:
                    if el != map[open_paren.pop()]:
                        return False
        
        return len(open_paren) == 0

s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("(}"))
print(s.isValid("(("))
