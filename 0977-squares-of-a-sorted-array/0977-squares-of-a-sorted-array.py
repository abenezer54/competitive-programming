class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = nums[i]**2
        # return sorted(nums
        left = 0
        right = len(nums) - 1
        ans = []
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                ans.append(nums[right]**2)
                right -= 1
            else:
                ans.append(nums[left]**2)
                left += 1
        return ans[::-1]