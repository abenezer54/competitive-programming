class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        length = len(nums)
        unreachable = 1
        i = ans = 0
        while unreachable <= n:
            if i < length:
                if unreachable >= nums[i]:
                    unreachable += nums[i]
                    i += 1
                else:
                    ans += 1
                    unreachable *= 2
            else:
                ans += 1
                unreachable *= 2

        return ans
        