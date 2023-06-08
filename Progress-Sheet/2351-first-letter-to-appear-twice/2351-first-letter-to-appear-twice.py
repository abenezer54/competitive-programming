class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
            if dic[char] == 2:
                return char