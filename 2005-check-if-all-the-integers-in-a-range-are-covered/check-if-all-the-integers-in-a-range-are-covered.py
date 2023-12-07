class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        domain = set()
        for a, b in ranges:
                domain.update(range(a, b + 1))

        return set(range(left, right + 1)) <= domain 