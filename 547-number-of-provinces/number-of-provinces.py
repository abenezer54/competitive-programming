class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = list(range(n))
        rank = [0] * n
        def find(v):
            while v != par[v]:
                v = par[v]
            return v
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    ri = find(i)
                    rj = find(j)
                    if ri != rj:
                        if rank[ri] > rank[rj]:
                            par[rj] = ri
                        elif rank[ri] < rank[rj]:
                            par[ri] = rj
                        else:
                            par[rj] = ri
                            rank[ri] += 1
        ans = 0
        for i in range(n):
            if i == find(i):
                ans += 1

        return ans
