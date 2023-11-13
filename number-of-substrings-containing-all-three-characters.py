class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0
        for right, char in enumerate(s):
            count[char] += 1
            while len(count) == 3:
                ans += len(s) - right 
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
                
        return ans