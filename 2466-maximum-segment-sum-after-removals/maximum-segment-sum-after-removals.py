class Dsu:
        def __init__(self, size, nums):
            self.parent = list(range(size))
            self.size = [nums[i] for i in range(size)]
    
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
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]
        dsu = Dsu(n, nums)
        mx = 0
        a = [-1] * n
        for i in range(n - 1, -1, -1):
            idx = removeQueries[i]
            a[idx] = i
            if 0 <= idx - 1 and a[idx - 1] != -1:
                dsu.union(idx, idx - 1)
            if idx + 1 < n and a[idx + 1] != -1:
                dsu.union(idx, idx + 1)
            root = dsu.find(idx)
            mx = max(mx, dsu.size[root])
            ans.append(mx)
        return ans[-2::-1]

        