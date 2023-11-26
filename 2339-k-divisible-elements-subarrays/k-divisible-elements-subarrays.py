class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        N = len(nums)
        check = set()

        for i in range(N):
            cur = 0
            strs = ""
            for j in range(i, N):
                if nums[j] % p == 0:
                    cur += 1
                strs += str(nums[j]) + ","  
                if cur > k:
                    break
                check.add(strs)

        return len(check)
        