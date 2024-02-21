class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, look = [], defaultdict(int)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                look[(stack[-1][0], stack[-1][1])] =  i - stack[-1][1]
                stack.pop()
            stack.append([temp, i])

        return [look[(temp, i)] for i, temp in enumerate(temperatures)]
        