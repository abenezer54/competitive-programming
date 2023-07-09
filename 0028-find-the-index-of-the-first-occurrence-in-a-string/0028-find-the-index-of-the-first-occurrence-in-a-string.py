class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(needle)
        l = 0
        r = n - 1
        while r < len(haystack):
            if haystack[l] == needle[0] and haystack[r] == needle[n - 1]:
                i = l + 1
                j = r - 1
                x = 1
                y = n - 2
                while i <= j:
                    if haystack[i] != needle[x] or haystack[j] != needle[y]:
                        break
                    else:
                        i += 1
                        j -= 1
                        x += 1
                        y -= 1
                if i > j:
                    return l
            l += 1
            r += 1
        return -1
