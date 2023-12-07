class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one = s.count("1")
        ans = ["0"] * len(s)
        for i in range(one - 1):
            ans[i] = "1"
        ans[-1] = "1"
        
        return "".join(ans)
        