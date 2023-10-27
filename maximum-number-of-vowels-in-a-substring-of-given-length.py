class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        left = 0
        count = 0
        ans = 0
        for right, char in enumerate(s):
            if char in vowels:
                count += 1
            if right > k - 2:
                ans = max(ans, count)
                if s[left] in vowels:
                    count -=1
                left += 1

        return ans