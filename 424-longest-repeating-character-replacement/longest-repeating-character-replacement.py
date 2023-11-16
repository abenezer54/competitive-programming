class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxLength = 0
        for right, char in enumerate(s):
            count[char] += 1
            summ = sum(count.values())
            maxx = max(count.values())
            diff = summ - maxx
            while diff > k:
                count[s[left]] -= 1
                summ = sum(count.values())
                maxx = max(count.values())
                diff = summ - maxx
                left += 1
            maxLength = max(maxLength, right - left +1)
        
        return maxLength
        