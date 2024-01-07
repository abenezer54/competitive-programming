class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        n = len(s)
        check = Counter(p)
        current = defaultdict(int)
        l = 0
        ans = []
        for r in range(n):
            current[s[r]] += 1

            if r >= k - 1:
                if current == check:
                    ans.append(l)
                current[s[l]] -= 1
                if current[s[l]] == 0:
                    current.pop(s[l])
                l += 1
                
        return ans
       