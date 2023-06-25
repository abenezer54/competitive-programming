class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0
        else:
            p1 = 0
            p2 = 1
            ans = 0
            while p2 < len(nums):
                if nums[p1] == nums[p2]:
                    p2 += 1
                else:
                    ans += 1
                    p1 += 1
                    p2 += 1
            return ans