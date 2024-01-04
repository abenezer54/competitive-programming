class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        l = 0
        r = n - 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum > k:
                r -= 1
            elif cur_sum < k:
                l += 1
            else:
                ans += 1
                l += 1
                r -= 1
    
        return ans
        