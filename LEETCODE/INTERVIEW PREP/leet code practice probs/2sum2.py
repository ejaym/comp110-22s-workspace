class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result_dict = {}
        for index, num in enumerate(nums):
            needednum = target - num
            if (needednum in result_dict):
                return [result_dict[needednum], index]
            else:
                result_dict[num] = index
        return [0]