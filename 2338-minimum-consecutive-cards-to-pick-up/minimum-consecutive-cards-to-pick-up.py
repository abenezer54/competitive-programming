class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l, n, ans, visited = 0, len(cards), float("inf"), set()
        for r in range(n):
            while cards[r] in visited:
                ans = min(ans, r - l + 1)
                visited.discard(cards[l])
                l += 1

            visited.add(cards[r])
        if ans == float("inf"):
            return -1
        return ans