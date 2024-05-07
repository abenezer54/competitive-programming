class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num

        idx = format(x, 'b')[::-1].index('1')
        y = 0
        for num in nums:
            if (1 << idx) & num:
                y ^= num

        return [y, x ^ y]
        