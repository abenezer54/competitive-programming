from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subArr = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subArr.append(sum(nums[i:j]))
        subArr.sort()
        ans = 0
        for i in range(left - 1, right):
            ans += subArr[i]
        return ans%1000000007
