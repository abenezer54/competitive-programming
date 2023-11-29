class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int: 
        # return (mainTank + (mainTank//5 if mainTank//5 <= additionalTank else additionalTank)) * 10
        consumed = 0
        while mainTank > 0:
            consumed += 1
            if consumed % 5 == 0 and additionalTank > 0:
                consumed += 1
                additionalTank -= 1
            mainTank -= 1
            
        return consumed * 10
