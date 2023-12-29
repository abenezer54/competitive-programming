class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                cur += 1
            ans += cur
        
        return ans