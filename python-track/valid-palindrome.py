class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    right -= 1
                    left += 1
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
        return True
        