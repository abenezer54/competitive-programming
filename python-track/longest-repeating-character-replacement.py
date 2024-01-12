class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, n, count, ans = 0, len(s), defaultdict(int), 0

        def check(count):
            tot = 0
            maxx = 0
            for v in count.values():
                maxx = max(maxx, v)
                tot += v
            return tot - maxx

        for r in range(n):
            count[s[r]] += 1
            while check(count) > k:
                if count[s[l]] == 1:
                    count.pop(s[l])
                else:
                    count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans       