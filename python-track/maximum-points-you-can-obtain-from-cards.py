class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        n = len(card)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + card[i]

        rs = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            rs[i] = rs[i + 1] + card[i]
        rs.reverse()

        ans = 0
        for i in range(k + 1):
            cur_sum = p[i] + rs[k - i]
            ans = max(ans, cur_sum)
            
        return ans
        