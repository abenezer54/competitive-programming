class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I" : 1, "V" : 5, "X": 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        ans = 0
        for char in s:
            ans += dic[char]
        return ans