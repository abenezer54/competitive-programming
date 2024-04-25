class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, x2, y1, y2 = points[i][0], points[j][0], points[i][1], points[j][1]
                d = abs(x1 - x2) + abs(y1 - y2)
                edges.append((d, i, j))
        edges.sort(key=lambda item: item[0])

        p = list(range(n))
        def find(a):
            root = a
            while root != p[root]:
                root = p[root]

            while a != root:
                nxt = p[a]
                p[a] = root
                a = nxt
            return root 

        def union(ra, rb):
            p[ra] = rb

        ans = 0
        for d, a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                union(ra, rb)
                ans += d
        return ans
