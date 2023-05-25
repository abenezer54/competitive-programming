class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        distances = []
        dic = defaultdict(list)
        for point in points:
            d = pow(point[0], 2) + pow(point[1], 2)
            distances.append(d)
        for i in range(len(distances)):
            dic[distances[i]].append(points[i])
        distances.sort()
        print(dic)
        ans = []
        i = 0
        j = 0
        while i < k:
            ans.extend(dic[distances[j]])
            j += 1
            i += len(dic[distances[j]])
        return ans