class Solution:
    def findComplement(self, num: int) -> int:
        s = list(bin(num))
        for i in range(2, len(s)):
            if s[i] == '0':
                s[i] = '1'
            else:
                s[i] = '0'
        s = ''.join(s)
        return int(s[2:], 2)
        