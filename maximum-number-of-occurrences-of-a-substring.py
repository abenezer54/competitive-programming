class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        ans = defaultdict(int)
        count = defaultdict(int)
        for right, num in enumerate(s):
            count[num] += 1
            while (right - left + 1) >= minSize and (right - left + 1) <= maxSize:
                if len(count) <= maxLetters:
                    ans[s[left:right + 1]] += 1
                count[s[left]] -= 1
                if not count[s[left]]:
                    count.pop(s[left])
                left += 1
                
        return max(ans.values()) if ans else 0