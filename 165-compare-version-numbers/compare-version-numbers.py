class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v = list(map(int, version1.split('.')))
        u = list(map(int, version2.split('.')))
        n, m = len(v), len(u)
        mx = max(n, m)
        v += [0] * (mx - n)
        u += [0] * (mx - m)
        for i in range(mx):
            if v[i] > u[i]:
                return 1
            if u[i] > v[i]:
                return -1
        return 0
