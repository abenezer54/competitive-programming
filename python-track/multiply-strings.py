class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strToInt(s):
            num = 0
            for c in s:
                num *= 10
                num += (ord(c) - ord("0") )
            return num
        def intToStr(num):
            s = ""
            while num > 0:
                s += (chr(ord("0") + num % 10))
                num //= 10
            return s[::-1]
            
        if num1 == "0" or num2 == "0":
            return "0"
        return intToStr(strToInt(num1) * strToInt(num2))
        