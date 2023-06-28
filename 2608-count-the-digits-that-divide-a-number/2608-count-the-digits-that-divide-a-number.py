class Solution:
    def countDigits(self, num: int) -> int:
        word = str(num)
        count = 0
        for i in range(len(word)):
            if num % int(word[i]) == 0:
                count += 1
        return count