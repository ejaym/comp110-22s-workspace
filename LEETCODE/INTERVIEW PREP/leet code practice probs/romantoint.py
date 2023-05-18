class Solution:
    def romanToInt(self, s: str) -> int:
        romanints = {}
        romanints['I'] = 1
        romanints['V'] = 5
        romanints['X'] = 10
        romanints['L'] = 50
        romanints['C'] = 100
        romanints['D'] = 500
        romanints['M'] = 1000
        i = 0
        result = 0
        while i < len(s):
            if i < len(s) - 1 and romanints[s[i]] < romanints[s[i + 1]]:
                result -= romanints[s[i]]
            else:
                result += romanints[s[i]]
            i += 1
        return result
