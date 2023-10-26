class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        dic = {"a": 0, "b": 0, "c": 0}
        left = 0     
        for right in range(len(s)):
            dic[s[right]] += 1          
            while all(dic.values()):
                ans += len(s) - right  
                dic[s[left]] -= 1
                left += 1
        
        return ans