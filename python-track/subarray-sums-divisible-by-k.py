class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1
        cur = ans = 0
        for num in nums:
            cur += num
            remainder = cur % k
            ans += count[remainder]
            count[remainder] += 1
        return ans
        