class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = odd = count = ans = 0

        for r in range(n):
            if nums[r] & 1:
                odd += 1
                count = 0
            while odd == k:
                count += 1
                if nums[l] & 1:
                    odd -= 1
                l += 1
            ans += count
        return ans
            