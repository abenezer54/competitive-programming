class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversedNum = 0
        while x > 0:
            reversedNum = (reversedNum * 10) + (x % 10)
            x //= 10
        return original == reversedNum