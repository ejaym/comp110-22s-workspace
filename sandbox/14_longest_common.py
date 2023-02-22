"""14 longest common prefix"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i: int = 0
        l: str = ""
        p: str = ""
        
        while(i < len(strs)):
            str(i) = ""
            
