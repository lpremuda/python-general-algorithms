'''
13. ROMAN TO INTEGER
https://leetcode.com/problems/roman-to-integer/
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        combos = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        sum = 0

        i = 0

        while i < len(s):
            # Check combo
            if i < len(s) - 1 and s[i:i+2] in combos.keys():
                sum += combos[s[i:i+2]]
                i += 2
            else:
                sum += map[s[i]]
                i += 1
             
        return sum

s = Solution()
print(s.romanToInt("IV"))
print(s.romanToInt("CIX"))
print(s.romanToInt("III"))