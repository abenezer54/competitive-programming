class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        p = list(range(n))
        size = [1] * n
        def find(a):
            root = a
            while root != p[root]:
                root = p[root]

            while a != root:
                nxt = p[a]
                p[a] = root
                a = nxt
            return root  
              
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                p[ra] = rb
                size[rb] += size[ra]

        x, y = defaultdict(int), defaultdict(int)
        for i in range(n):
            a, b = stones[i]
            if a in x:
                union(i, x[a])
            else:
                x[a] = i

            if b in y:
                union(i, y[b])
            else:
                y[b] = i
      
        ans = 0
        for i in range(n):
            if i == find(i):
                ans += size[i] - 1
        return ans







