class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        l, true, false, n = 0, 0, 0, len(s)
        ans = 0
        for r in range(n):
            if s[r] == "T":
                true += 1
            else:
                false += 1
            while min(true, false) > k:
                if s[l] == "T":
                    true -= 1
                else:
                    false -= 1
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans
