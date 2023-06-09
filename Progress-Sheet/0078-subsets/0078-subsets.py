from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            p = list(combinations(nums, i))
            for j in p:
                ans.append(list(j))
        return ans
