class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        suffix = [1] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] * nums[i]
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        ans = [0] * n
        for i in range(n):
            ans[i] = prefix[i] * suffix[i + 1]
            
        return ans
