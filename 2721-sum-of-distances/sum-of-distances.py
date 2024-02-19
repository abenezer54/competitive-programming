class Solution:
    def distance(self, a: List[int]) -> List[int]:
        n = len(a)
        prefix = {}
        ans = [0] * n
        for i in range(n):
            if a[i] not in prefix:
                prefix[a[i]] = [1, i]
            else:
                ans[i] += (i * prefix[a[i]][0]) - prefix[a[i]][1]
                prefix[a[i]][0] += 1
                prefix[a[i]][1] += i             
        
        suffix = {}
        for i in range(n - 1, -1, -1):
            if a[i] not in suffix:
                suffix[a[i]] = [1, n - i]
            else:
                ans[i] +=  ((n - i) * suffix[a[i]][0]) - suffix[a[i]][1]
                suffix[a[i]][0] += 1
                suffix[a[i]][1] += n - i
                
        return ans
        