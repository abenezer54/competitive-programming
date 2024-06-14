class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            r = cur % k
            if r in mp and i - mp[r] > 1:
                return True
            elif r in mp:
                continue
            else:
                mp[r] = i
        return False    
