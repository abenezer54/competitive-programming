class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        ans = left = max_count = 0
        for right, char in enumerate(s):
            dic[char] += 1
            max_count = max(max_count, dic[char])
            diff = right - left + 1 - max_count
            while diff > k:
                dic[s[left]] -= 1
                left += 1
                max_count = max(dic.values())
                diff = right - left + 1 - max_count  
            ans = max(ans, right - left + 1)

        return ans