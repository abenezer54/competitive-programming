class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        c = 1 - flips[0]
        maxx = flips[0]
        ans = 0
        if c == 0:
            ans += 1
        
        for i in range(1, n):
            if flips[i] > maxx:
                c -= flips[i] - maxx - 1
                maxx = flips[i]
            else:
                c += 1

            if c == 0:
                ans += 1 
        return ans
                    