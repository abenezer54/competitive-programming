class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        m = len(queries)
        edges.sort(key=lambda item: item[2])
        queries = sorted([queries[i] + [i] for i in range(m)], key=lambda item: item[2])
        ans = [False] * m
        p = list(range(n + 1))
        r = [0] * (n + 1)
        def find(a):
            rt = a
            while rt != p[rt]:
                rt = p[rt]

            while a != rt:
                nxt = p[a]
                p[a] = rt
                a = nxt
            return rt

        def union(a, b):
            rta, rtb = find(a), find(b)
            if rta != rtb:
                if r[rta] > r[rtb]:
                    p[rtb] = rta
                elif r[rta] < r[rtb]:
                    p[rta] = rtb
                else:
                    p[rta] = rtb
                    r[rtb] += 1

        i = 0
        for a, b, limit, idx in queries:
            while i < len(edges) and edges[i][2] < limit:
                union(edges[i][0], edges[i][1])
                i += 1
            if find(a) == find(b):
                ans[idx] = True
                
        return ans
    
        