class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [ 'a', 'e', 'i', 'o', 'u']
        s = [char for char in s]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[right], s[left] = s[left], s[right]
                right -= 1
                left += 1
        
        return "".join(s)