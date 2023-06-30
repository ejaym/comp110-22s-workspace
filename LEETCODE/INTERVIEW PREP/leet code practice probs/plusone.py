class Solution: #this almost passes all test cases but there are errors in the edge case that you are given mutliple 9's in a list in a row
    def plusOne(self, digits: List[int], carry: int = 0) -> List[int]:
        lastdigitofint = digits[-1]
        lastdigitofint += 1
        if (lastdigitofint < 10):
            digits[-1] = lastdigitofint
            return digits
        if (lastdigitofint % 10 != 0 and len(digits) > 1):
            inplace = lastdigitofint % 10
            carry = lastdigitofint // 10
            digits[-1] = inplace
            return plusOne(digits[0:len(digits) - 1], carry)
        else:
            digits[-1] = lastdigitofint
            return digits
        

#TODO ACTUAL SOLUTION TO LEARN FROM

"""class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        for i in reversed(range(n)):
            val = digits[i] + carry + 1 if i == n-1 else digits[i] + carry
            if val <= 9:
                digits[i] = val
                carry = 0
            else:
                carry = val // 10
                val -= 10
                digits[i] = val
        if carry:
            digits.insert(0, carry)
        return digits"""