class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p = defaultdict(str)
        rank = defaultdict(int)
        n = len(s1)
        for i in range(26):
            char = chr(97 + i)
            p[char] = [char, char]
            
        def find(a):
            root = a
            while root != p[root][0]:
                root = p[root][0]
            
            while a != root:
                nxt = p[a][0]
                p[a][0] = root
                a = nxt

            return root
            
        def union(a, b):
            ra, rb = find(a), find(b)

            if ra != rb:
                if rank[ra] > rank[rb]:
                    p[rb][0] = ra
                    p[ra][1] = min(p[rb][1], p[ra][1]) 
                elif rank[ra] < rank[rb]:
                    p[ra][0] = rb
                    p[rb][1] = min(p[rb][1], p[ra][1]) 
                else:
                    p[rb][0] = ra
                    p[ra][1] = min(p[rb][1], p[ra][1]) 
                    rank[ra] += 1

        for i in range(n):
            union(s1[i], s2[i])

        ans = []
        for char in baseStr:
            root = find(char)
            ans.append(p[root][1])
        
        return ''.join(ans)
        