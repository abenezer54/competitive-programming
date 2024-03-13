class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n, ans = len(nums), 0
        for i in range(n):
            minn = nums[i]
            maxx = target - minn
            idx = bisect_right(nums, maxx, i + 1)
            if nums[i] + nums[idx - 1] <= target:
                ans += (pow(2, idx - i - 1)) % (pow(10, 9) + 7)
            else:
                break
        return ans % (pow(10, 9) + 7)
        