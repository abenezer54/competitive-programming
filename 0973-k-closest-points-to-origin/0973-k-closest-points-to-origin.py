class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        points = sorted(points, key = lambda x : sqrt(x[0]**2 + x[1]**2))
        return points[:k]
#         from math import sqrt
#         distances = []
#         dic = {}
#         for point in points:
#             d = abs(sqrt(pow(point[0], 2) + pow(point[1], 2)))
#             distances.append(d)
#         for i in range(len(distances)):
#             dic[distances[i]] = points[i]
#         distances.sort()
        
#         ans = []
#         for i in range(k):
#             ans.append(dic[distances[i]])
#         return ans