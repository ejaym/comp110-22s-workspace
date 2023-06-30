class Solution:
    def isHappy(self, n: int) -> bool:
        strn = str(n)
        lengthofnum = len(strn)
        if n == 1 or n == 7:
            return True
        if lengthofnum == 1:
            return False
        i = 0
        while n != 1:
            individualnums = n
            n = 0 
            for nums in str(individualnums):
                nums = int(nums)
                n += nums ** 2
            if n != 1:
                i += 1
                if i == 100:
                    return False
        else:
            return True


