class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        check = []       
        while n >= 0:
            a = n
            count = 0
            while a >= 3:
                count += 1
                a //= 3

            a = n
            if count in check:
                a -= pow(3, count - 1)
            else:
                a -= pow(3, count)
                check.append(count)
            if a == 0:
                return True
            n = a

        return False