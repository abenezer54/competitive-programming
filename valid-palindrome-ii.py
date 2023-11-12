class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[right] == s[left]:
                left += 1
                right -= 1
            else:
                word = list(s[left + 1:right + 1])
                if word == word[::-1]:
                    return True
                else:
                    word.pop()
                    word.insert(0,s[left])
                    if word == word[::-1]:
                        return True
                    return False

        return True