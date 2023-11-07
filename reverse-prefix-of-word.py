class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        for right, char in enumerate(word):
            if char == ch:
                left = 0
                while left < right:
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
                break
        
        return "".join(word)