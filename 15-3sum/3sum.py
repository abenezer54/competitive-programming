class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                cur_sum = nums[l] + nums[r]

                if cur_sum + nums[i] == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif cur_sum + nums[i] < 0:
                    l += 1
                else:
                    r -= 1
      
        return list(ans)
        