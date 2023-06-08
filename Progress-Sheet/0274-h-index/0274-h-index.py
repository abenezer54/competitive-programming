class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)  
        for citation in citations:
            if citation >= n:
                count[n] += 1
            else:
                count[citation] += 1
        print(count)

        total = 0
        ans = 0

        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                ans = i
                break

        return ans
