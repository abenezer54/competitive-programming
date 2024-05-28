class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def get_bits(n):
            n &= 0xffffffff
            bits = f'{n:032b}'
            return bits
        root, mp = {}, {}
        for num in nums:
            bits = get_bits(num)
            mp[num] = bits
            cur = root
            for bit in bits:
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]

        opp = {'0':'1', '1':'0'}
        maxx = 0
        for num in nums:
            bits = mp[num]
            cur = root
            res = 0
            for i, bit in enumerate(bits):
                if opp[bit] in cur:
                    res += 1 << (32 - i - 1)
                    cur = cur[opp[bit]]
                else:
                    cur = cur[bit]
            maxx = max(maxx, res)
        return maxx
