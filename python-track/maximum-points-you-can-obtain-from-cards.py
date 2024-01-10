class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        cur = sum(card[:k])
        ans = cur
        r = k - 1
        l = 0
        while r > -1:
            cur -= card[r]
            r -= 1
            l -= 1
            cur += card[l]
            ans = max(ans, cur)

        return ans
        