class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        k = sum(nums) % p
        print('k,', k)
        if sum(nums) < p:
            return -1
        if k == 0:
            return 0

        count = {0: -1}
        cur = 0
        ans = float('inf')
        for i in range(n):        
            cur += nums[i]
            # print(cur)
            r = cur % p
            if (r - k) % p in count:
                if count[(r - k)% p] != -1 or i != n - 1:
                    ans = min(ans, i - count[(r - k) % p] )
         
            if r in count:
                count[r] = max(count[r], i)
            else:
                count[r] = i

        if ans == float('inf'):
            return -1
        return ans