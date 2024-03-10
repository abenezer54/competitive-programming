class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(mid):
            nonlocal threshold
            tot = 0
            for num in nums:
                tot += ceil(num / mid)
            return tot <= threshold

        l, r = 0, max(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid
        return r