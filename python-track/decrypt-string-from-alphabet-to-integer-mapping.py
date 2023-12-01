class Solution:
    def freqAlphabets(self, s: str) -> str:
        c = 96
        ans = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                n = int(s[i - 2:i])
                ans += chr(c + n)
                i -= 3
            else:
                ans += chr(c + int(s[i]))
                i -= 1
        return ans[::-1]
        