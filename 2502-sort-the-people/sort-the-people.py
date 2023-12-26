class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        look = {heights[i]:names[i] for i in range(len(names))}
        for i in range(n):
            for j in range(0,n - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]

        for i in range(n):
            names[i] = look[heights[i]]

        return names
        