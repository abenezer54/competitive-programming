class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        max_len = max(len(w) for w in forbidden)
        n = len(word)
        ans = l = 0
        for r in range(n):
            for i in range(max(l, r - max_len - 1), r + 1):
                if word[i: r + 1] in forbidden:
                    l = i + 1
            ans = max(ans, r - l + 1)
        return ans
        