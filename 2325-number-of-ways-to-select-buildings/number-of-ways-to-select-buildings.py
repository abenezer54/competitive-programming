class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        ans = 0
        sz = [0] * (n + 1)
        so = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                sz[i] = 1 + sz[i + 1]
                so[i] = so[i + 1]
            else:
                sz[i] = sz[i + 1]
                so[i] = 1 + so[i + 1]
        pz = 0
        po = 0
        for i in range(n - 1):
            if i > 0:
                if s[i] == "0":
                    ans += po * so[i + 1]
                else:
                    ans += pz * sz[i + 1]
            
            if s[i] == "0":
                pz += 1
            else:
                po += 1
        return ans