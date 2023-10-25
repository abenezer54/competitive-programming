class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        N = len(p)
        ans = []

        for i in range(len(s) - N + 1):
            print(i)
            check = Counter(s[i : i + N])
            if check == target:
                ans.append(i)
        return ans