class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        p = [0] * (n + 1)
        ss = list(s)
        
        for s, e, d in shifts:
            if d:
                p[s] += 1
                p[e + 1] -= 1
            else:
                p[s] -= 1
                p[e + 1] += 1

        for i in range(1,  n + 1):
            p[i] += p[i - 1]
        
        for i in range(n):
            cur = ord(ss[i])
            new = ((cur - 96 ) + p[i]) % 26
            if new == 0:
                ss[i] = 'z'
            else:
                ss[i] = chr(new + 96)

        return ''.join(ss)
                