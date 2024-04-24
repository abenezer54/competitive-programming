class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        n = len(strs)
        p = defaultdict(str)
        rank = defaultdict(int)

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
            if rank[ra] > rank[rb]:
                p[rb] = ra
            elif rank[ra] < rank[rb]:
                p[ra] = rb
            else:
                p[rb] = ra
                rank[ra] += 1

        ans = n
        m = len(strs[0])
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if strs[i][k] != strs[j][k]:
                        cnt += 1
                        if cnt > 2:
                            break
                if cnt <= 2:
                    if strs[i] not in p:
                        p[strs[i]] = strs[i]
                    if strs[j] not in p:
                        p[strs[j]] = strs[j]
                    ra, rb = find(strs[i]), find(strs[j])

                    if ra != rb:
                        union(ra, rb)
                        ans -= 1

        return ans 
