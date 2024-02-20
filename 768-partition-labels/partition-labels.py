class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def check(dic, count):
            for k, v in dic.items():
                if count[k] != v:
                    return False
            return True
            
        count, cur, n, l = Counter(s), Counter(), len(s), 0
        ans = []
        for i in range(n):
            cur[s[i]] += 1
            if check(cur, count):
                ans.append(i - l + 1)
                l = i + 1
        return ans
        