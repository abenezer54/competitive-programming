class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        p = list(range(n))
        order = defaultdict(str)
        for i in range(n):
            order[i] = s[i]

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

        for a, b in pairs:
            union(a, b)

        mp = defaultdict(list)
        for i in range(n):
            mp[find(i)].append(i)
        
        for row in mp.values():
            row.sort(reverse=True, key=lambda item: order[item])
        
        ans = []
        for i in range(n):
            rt = find(i)
            ans.append(s[mp[rt].pop()])
        
        return ''.join(ans)
        
        

        