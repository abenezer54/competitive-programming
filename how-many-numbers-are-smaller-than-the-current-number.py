class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedList = sorted(nums)
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            ans[i] = sortedList.index(num)

        return ans