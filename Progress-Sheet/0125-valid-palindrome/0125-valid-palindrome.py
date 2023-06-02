class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [char.lower() for char in s if char.isalnum()]
        print(arr)
        left = 0
        right = len(arr) - 1
        isPal = True
        while left <= right:
            if arr[left] != arr[right]:
                isPal = False
            left += 1
            right -= 1
        return True if isPal else False