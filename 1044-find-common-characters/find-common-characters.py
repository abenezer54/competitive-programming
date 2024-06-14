class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mn = [float('inf')] * 26
        for word in words:
            cnt = Counter(word)
            for i in range(26):
                mn[i] = min(mn[i], cnt[chr(i + 97)])
        ans = []
        for i in range(26):
            if mn[i]:
                ans.extend([chr(i + 97)] * mn[i])
        return ans