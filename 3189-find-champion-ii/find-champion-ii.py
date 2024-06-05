class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ind = [0] * n
        for x, y in edges:
            ind[y] += 1
        return ind.index(0) if ind.count(0) == 1 else -1
