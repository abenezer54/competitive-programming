class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        c = Counter(s1)
        l = 0
        curr = defaultdict(int)
        for r in range(n):
            curr[s2[r]] += 1
            if r >= k - 1:
                if curr == c:
                    return True
                curr[s2[l]] -= 1

                if curr[s2[l]] == 0:
                    curr.pop(s2[l])
                l += 1
        return False

        