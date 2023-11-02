class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
            
        ans = -1
        for i in range(1, len(prefix)):
            if prefix[i  - 1] == (prefix[-1] - prefix[i ]):
                ans = i - 1
                break

        return ans