class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l = 0
            r = len(word) - 1
            is_palindrome = True  
            while l < r:
                if word[l] != word[r]:
                    is_palindrome = False
                    break 
                l += 1
                r -= 1
            if is_palindrome:  
                return word
        return ""
                
        
