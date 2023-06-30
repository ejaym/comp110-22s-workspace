class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        resultdict = {}
        for numbers in nums:
            if (numbers in resultdict):
                resultdict[numbers] += 1
            else:
                resultdict[numbers] = 1
        for numbers in nums:
            while (resultdict[numbers] != 1):
                resultdict[numbers] -= 1
                indextopop = nums.index(numbers)
                nums.pop(indextopop)
        return len(nums)

    
wowie: Solution = Solution()
print(Solution.removeDuplicates(wowie, [1, 1, 2]))    