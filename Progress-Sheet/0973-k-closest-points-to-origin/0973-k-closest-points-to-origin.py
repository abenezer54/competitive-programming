class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        points = sorted(points, key = lambda x : sqrt(x[0]**2 + x[1]**2))
        return points[:k]
