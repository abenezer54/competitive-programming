class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(a):
            root = a
            while root != p[root]:
                root = p[root]

            while a != root:
                nxt = p[a]
                p[a] = root
                a = nxt
            return root


        def union(r1, r2):
            if rank[r1] > rank[r2]:
                p[r2] = r1
            elif rank[r2] > rank[r1]:
                p[r1] = r2
            else:
                p[r1] = r2
                rank[r2] += 1


        for a, b in edges:
            r1, r2 = find(a), find(b)
            if r1 == r2:
                return [a, b]
            union(r1, r2)
                