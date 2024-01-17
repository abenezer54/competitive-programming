class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1]  = p[i] + nums[i]
        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + nums[i]
        for i in range(n):
            if p[i] == s[i + 1]:
                return i

        return -1
       
        