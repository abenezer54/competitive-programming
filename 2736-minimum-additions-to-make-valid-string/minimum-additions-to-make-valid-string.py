class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        for i in range(1, len(word)):
            diff = ord(word[i]) - ord(word[i - 1])
            if diff == 0:
                ans += 2
            elif diff == - 1 or diff == 2:
                ans += 1
                
        if word[0] == "b":
            ans += 1
        if word[0] == "c" :
            ans += 2
        if word[-1] == "a":
            ans += 2
        if word[-1] == "b":
            ans += 1

        return ans  
                