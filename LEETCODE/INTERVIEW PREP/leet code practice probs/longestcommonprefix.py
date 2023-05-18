class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        letterindex = 0
        first_word = strs[0]
        returnpre = ""
        while (i < len(strs)):
            if (first_word == strs[i]):
                i += 1
            else:
                letterindex = 0
                if (len(first_word) < len(strs[i])):
                    shortestwordindex = len(first_word)
                else:
                    shortestwordindex = len(strs[i])
                while (letterindex < shortestwordindex):
                    if (first_word[letterindex] != strs[i][letterindex]):
                        letterindex += 1
                    else:
                        returnpre += first_word[letterindex]
                        letterindex += 1
                i += 1
        return returnpre
    
    # A very close attempt at getting it to work but does not work as it adds all the prefixes that the first word has in common with every other word into a single string, which is not correct.
    
   
    #TODO The actual solution is as follows:
    # class Solution:
    # def longestCommonPrefix(self, strs: list[str]) -> str:
    #     if len(strs) == 0:
    #         return ""

    #     prefix = ""
    #     first_word = strs[0]
        
    #     #Letter index cannot be greater than the len of a string at a given index because a prefix must be shorter than the length of a word its being compared to
    #     for letterindex in range(len(first_word)):
    #         for i in range(1, len(strs)):
    #             if letterindex >= len(strs[i]) or first_word[letterindex] != strs[i][letterindex]:    #in this line we stop whenever a missmatch is found because that is the smallest common prefix that every word has in common
    #                 return prefix
    #         prefix += first_word[letterindex] #If for none of the first/2nd/3rd/ect letters of all words violate the if statement above, the letter is added to the prefix
            
    #     return prefix