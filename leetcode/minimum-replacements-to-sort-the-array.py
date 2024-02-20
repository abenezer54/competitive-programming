class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last, n, ans = nums[-1], len(nums), 0

        for i in range(n - 2, -1, -1):
            if nums[i] > last:        
                length = ((nums[i] - 1) // last) + 1
                last = nums[i] // length
                ans += length - 1
            else:
                last = nums[i]
            
        return ans