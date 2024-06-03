class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix = [[0] * maximumBit for _ in range(len(nums))]
        for i, num in enumerate(nums):
            for bit in range(maximumBit):
                if i > 0:
                    prefix[i][bit] += prefix[i - 1][bit]
                if num & (1 << bit):
                    prefix[i][bit] += 1

        ans = []
        for i in range(len(nums)):
            cur = 0
            for bit in range(maximumBit):
                if not (prefix[i][bit] & 1):
                    cur |= 1 << bit
            ans.append(cur)
            
        return ans[::-1]
        