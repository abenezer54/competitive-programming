class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["a", "A", "E", "e", "i", "I", "o", "O", "u", "U"]
        l = 0
        r = len(s) - 1
        arr = [char for char in s]
        while l < r:
            if arr[l] in vowel and arr[r] in vowel:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            else:
                if arr[l] not in vowel:
                    l += 1
                elif arr[r] not in vowel:
                    r -= 1
            
        return "".join(arr)
