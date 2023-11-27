class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        check = []
        for u, v in edges:
            if u in check:
                return u
            elif v in check:
                return v
            else:
                check.extend([u,v])