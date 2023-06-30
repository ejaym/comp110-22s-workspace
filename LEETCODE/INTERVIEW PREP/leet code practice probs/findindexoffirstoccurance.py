class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sizeofneedle = len(needle)
        i = 0
        areatosearch = sizeofneedle
        if (len(haystack) < len(needle)):
            return -1
        while len(haystack) - i >= sizeofneedle:
            if (haystack[i:areatosearch] == needle):
                return i
            else:
                i += 1
                areatosearch += 1
        return -1