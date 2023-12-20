class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = len(digits) - 1
            while i >= 0:
                if digits[i] != 9:
                    digits[i] += 1
                    break
                else:
                    digits[i] = 0
                i -= 1
            else:
                return [1] + digits
        else:
            digits[-1] += 1

        return digits
        