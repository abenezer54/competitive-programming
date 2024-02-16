class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        p = list(palindrome)
        l = 0
        h = n // 2
        while l < h:
            if p[l] != "a":
                p[l] = 'a'
                break
            l += 1
        else:
            p[-1] = 'b'
            return '' if n == 1 else "".join(p)
        return ''.join(p)

        