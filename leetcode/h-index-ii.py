class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def find_citations(paper):
            idx = bisect_left(citations, paper)
            return len(citations) - idx
        l, r = 0, len(citations) + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if find_citations(mid) >= mid:
                l = mid
            else:
                r = mid
        return l
        