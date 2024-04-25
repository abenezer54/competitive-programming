class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        p = list(range(n + 1))
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


        for a, b, d in roads:
            ra = find(a)
            rb = find(b)
            if ra != rb:
                union(ra, rb)

        ans = float('inf')
        for a, b, d in roads:
            ra = find(a)
            r1 = find(1)
            if ra == r1:
                ans = min(ans, d)
        
        return ans