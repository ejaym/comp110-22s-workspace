""""This question is confusing and doesn't really make sense."""
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        
    def add(self, val: int) -> int:
        i = 1
        self.nums.append(val)
        print(self.nums)
        maxint = max(self.nums)
        kthlarge: int
        if (self.k == 1):
            return maxint
        if (len(self.nums) < 2 or self.k not in range(len(self.nums))):
            return -1
        while i <= self.k:
            if (i == self.k and maxint - i not in self.nums):
                return -1
            if (maxint - i in self.nums):
                kthlarge = maxint - i
                i += 1
            else:
                return -1
        return kthlarge + 1


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(4, [1,2,3,4])
print(obj.add(5))
print(obj.nums)