class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = []
        for i in range(0, c + 1):
            squares.append(pow(i, 2))
            if pow(i, 2) >= c:
                break

        l = 0
        r = len(squares) - 1
        while l <= r:
            if squares[l] + squares[r] == c:
                return True
            if squares[l] + squares[r] < c:
                l += 1
            elif squares[l] + squares[r] > c:
                r -= 1
        return False