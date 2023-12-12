class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        check = set(nums)
        ans = 0
        for num in nums:
            n = num
            right_count = 0
            left_count = 0
            
            if num not in seen:
                while num + 1 in check:
                    right_count += 1
                    num += 1
                    seen.add(num)

                while n - 1 in check:
                    left_count += 1
                    n -= 1
                    seen.add(n)

            seen.add(num - right_count)
            ans = max(ans, left_count + right_count + 1)

        return ans
        