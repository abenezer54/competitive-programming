class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxx = nums[0]
        for i in range(1, n):
            cur_min = i
            cur_max = i + nums[i]
            if cur_min > maxx:
                return False
            maxx = max(maxx, cur_max)
        return True
        