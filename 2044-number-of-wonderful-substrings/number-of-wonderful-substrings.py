class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = mask = 0
        cnt = Counter()
        cnt[0] = 1

        for ch in word:
            idx = ord(ch) - ord('a')
            mask ^= 1 << idx
            ans += cnt[mask]

            for i in range(10):
                preMask = mask ^ (1 << i)
                ans += cnt[preMask]
            cnt[mask] += 1
        
        return ans
