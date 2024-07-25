class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        prefix.pop(0)

        ans = 0
        for sm in prefix:
            if lower <= sm <= upper:
                ans += 1
        
        def merge(left, right):
            nonlocal ans
            l = r = 0
            for num in left:
                while l < len(right) and right[l] - num < lower:
                    l += 1
                while r < len(right) and right[r] - num <= upper:
                    r += 1
                ans +=  r - l

            return sorted(left + right)
        
        def divide(arr):
            if len(arr) == 1:
                return arr

            mid = len(arr) // 2

            left = divide(arr[:mid])
            right = divide(arr[mid:])
            return merge(left, right)
        divide(prefix)
        return ans
        