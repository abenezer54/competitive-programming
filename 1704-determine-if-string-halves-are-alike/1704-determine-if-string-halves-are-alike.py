class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)// 2
        str1 = s[:n]
        str2 = s[n:]
        count1 = 0
        count2 = 0
        for char in str1:
            if char in vowels:
                count1 += 1
        for char in str2:
            if char in vowels:
                count2 += 1
        return True if count1 == count2 else False