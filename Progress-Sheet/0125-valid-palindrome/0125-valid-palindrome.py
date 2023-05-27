class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        newString = "".join([char for char in s if char.isalnum()])
        reversedString = newString[::-1]  
        ans = False if not newString == reversedString else True
        
        return ans