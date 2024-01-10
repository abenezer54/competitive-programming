class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, cur, ans, n = 0, 0, float("inf"), len(blocks)
        for r in range(n):
            if blocks[r] == "W":
                cur += 1
            if r >= k - 1:
                ans = min(ans, cur)
                if blocks[l] == "W":
                    cur -= 1
                l += 1
        return ans

        