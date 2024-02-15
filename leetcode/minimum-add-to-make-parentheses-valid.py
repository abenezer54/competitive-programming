class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o = 0
        c = 0
        for i, char in enumerate(s):
            if char == ")":
                if o > 0:
                    o -= 1
                else:
                    c += 1
            else:
                o += 1
                
        return o + c
        