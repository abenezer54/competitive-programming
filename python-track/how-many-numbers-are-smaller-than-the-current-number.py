class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        lookup = defaultdict(list)
        for i in range(len(nums)):
            lookup[sorted_nums[i]].append(i)

        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = lookup[nums[i]][0]
        
        return ans
        