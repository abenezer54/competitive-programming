class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        positive_pointer = 0
        negative_pointer = 1
        ans = [0] * N

        for num in nums:
            if num > 0:
                ans[positive_pointer] = num
                positive_pointer += 2
            else:
                ans[negative_pointer] = num
                negative_pointer += 2
                
        return ans
        