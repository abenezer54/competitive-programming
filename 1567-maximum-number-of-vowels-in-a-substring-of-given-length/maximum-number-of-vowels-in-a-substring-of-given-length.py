class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        n = len(s)
        l = ans = count = 0
        for r in range(n):
            if s[r] in vowel:
                count += 1
            if r >= k - 1:
                ans = max(ans, count)
                if s[l] in vowel:
                    count -= 1
                l += 1
        return ans
        