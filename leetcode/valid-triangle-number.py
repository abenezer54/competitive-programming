class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n, ans = len(nums), 0

        for cur in range(n - 1, 1, -1):
            right = cur - 1
            left = 0
            while left < right:
                if nums[left] + nums[right] > nums[cur]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1

        return ans
        