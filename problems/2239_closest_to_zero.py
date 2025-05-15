from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        i = nums[0]
        for num in nums:
            if abs(num) <= abs(i):
                # in the case we find a number with an abs value lower than the current one
                # we need to check if it's the same number but with an opposite signal
                if abs(num) == i:
                    # if it is, we just get the positive one
                    i = max(num, i)
                else:
                    i = num

        return i


sl = Solution()
mynums: List[int] = [2, -1, 1]
print(sl.findClosestNumber(mynums))
