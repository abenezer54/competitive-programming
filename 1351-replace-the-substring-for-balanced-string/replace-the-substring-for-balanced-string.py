class Solution:
    def balancedString(self, s: str) -> int:
        def check(curr, off):
            for key, val in off.items():
                if curr[key] < val:
                    return False
            return True

        n, k, count = len(s), len(s) // 4, Counter(s)
        off = defaultdict(int)
        for val in  "QWER":
            if count[val] > k:
                off[val] = count[val] - k
        if not off:
            return 0

        curr = defaultdict(int)
        l, ans = 0, float("inf")
        for r in range(n):
            curr[s[r]] += 1
            while check(curr, off):
                ans = min(ans, r - l + 1)
                curr[s[l]] -= 1
                if not curr[s[l]]:
                    curr.pop(s[l])
                l += 1
        return ans    
