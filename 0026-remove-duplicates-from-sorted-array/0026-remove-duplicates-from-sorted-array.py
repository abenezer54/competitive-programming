class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = len(nums) - 1
        s1 = 0
        s2 = 1
        if len(nums) == 1:
            return len(nums)
        else:
            while s2 <= p:
                if nums[s1] == nums[s2]:
                    del nums[s2]
                    p -= 1
                else:
                    s2 += 1
                    s1 += 1
        return len(nums)
