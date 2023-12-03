class Solution:
    def isWinner(self, p1: List[int], p2: List[int]) -> int:
        s1 = s2 = 0
        n = len(p1)
        for i in range(n):
            s1 += p1[i]
            s2 += p2[i]
        if n > 1:
            for i in range(1, n):
                if p1[i - 1] == 10 or ((i >= 2) and p1[i - 2] == 10):
                    s1 += p1[i]
                if p2[i - 1] == 10 or ((i >= 2) and p2[i - 2] == 10):
                    s2 += p2[i]
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        return 0        
        