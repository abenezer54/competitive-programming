class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # print(nums)
        def lessOrEqual(a, k):
            l, ans, count, cur, n = 0, 0, 0, 0, len(a)
            if k == -1:
                cur = -2
            for r in range(n):
                cur += a[r]
                count += 1
                while cur > k:
                    # print(cur, k)
                    cur -= a[l]
                    count -= 1
                    l += 1
                if k == -1:
                    count = 0
                ans += count
            # print(ans)
            return ans
        return lessOrEqual(nums, goal) - lessOrEqual(nums, goal - 1)