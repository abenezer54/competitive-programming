class dsu:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1 for i in range(size)]
 
    def find(self, x):
        rt = x
        while rt != self.parent[rt]:
            rt = self.parent[rt]

        while x != rt:
            nxt = self.parent[x]
            self.parent[x] = rt
            x = nxt
        return rt
 
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
 
        if px != py:
            if self.size[px] > self.size[py]:
                px, py = py, px
            self.parent[px] = py
            self.size[py] += self.size[px]
 
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob, both = [], [], []
        for t, a, b in edges:
            if t == 1:
                alice.append((a, b))
            elif t == 2:
                bob.append((a, b))
            else:
                both.append((a, b))

        ans = 0
        ag = dsu(n + 1)
        bg = dsu(n + 1)
        for x, y in both:
            if not ag.connected(x, y):
                ag.union(x, y)
                bg.union(x, y)
            else:
                ans += 1
        for x, y in alice:
            if not ag.connected(x, y):
                ag.union(x, y)
            else:
                ans += 1

        check = ag.find(1)
        for i in range(2, n + 1):
            rt = ag.find(i)
            if rt != check:
                return -1
            
        for x, y in bob:
            if not bg.connected(x, y):
                bg.union(x, y)
            else:
                ans += 1

        check = bg.find(1)
        for i in range(2, n + 1):
            rt = bg.find(i)
            if rt != check:
                return -1

        return ans