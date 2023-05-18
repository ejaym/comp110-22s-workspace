class Solution: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        intdict = {}
        for index, numbers in enumerate(nums):
            neededtoaddtotarget = target - numbers
            if (neededtoaddtotarget in intdict):
                return [intdict[neededtoaddtotarget], index]
            intdict[numbers] = index
        return [0]
    