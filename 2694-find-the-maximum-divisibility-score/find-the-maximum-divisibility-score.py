class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxx = 0
        ans = float("inf")

        for i in range(len(divisors)):
            cur = 0
            for num in nums:
                if num % divisors[i] == 0:
                    cur += 1
            if cur > maxx:
                ans = divisors[i]
                maxx = cur
            elif cur == maxx:
                ans = min(ans, divisors[i])

        return ans
        