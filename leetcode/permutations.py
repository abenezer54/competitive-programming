class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, permutation = [], []
        def backtrack(index):
            if len(permutation) == len(nums):
                ans.append(permutation[:])
            for i in range(len(nums)):
                if nums[i] not in permutation:
                    permutation.append(nums[i])
                    backtrack(i + 1)
                    permutation.pop()
        backtrack(0)
        return ans
        