class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        arr = [[position[i], speed[i]] for i in range(n)]
        arr.sort()
        stack = []
        for p, s in arr:
            while stack and ((target - stack[-1][0]) / stack[-1][1]) <= ((target - p) / s):
                stack.pop()
            stack.append([p, s])

        return len(stack)
        