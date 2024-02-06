class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tot = len(set(nums))
        l = ans = 0
        cur = Counter()
        for r in range(len(nums)):
            cur[nums[r]] += 1
            while len(cur) == tot:
                cur[nums[l]] -= 1
                if not cur[nums[l]]:
                    cur.pop(nums[l])
                l += 1
                ans += len(nums) - r
        return ans
        