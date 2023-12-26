class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        look = {heights[i]:names[i] for i in range(len(names))}
        for i in range(n):
            min_idx = i
            for j in range(i + 1,n ):
                if heights[min_idx] < heights[j]:
                    min_idx = j
            heights[min_idx], heights[i] = heights[i], heights[min_idx]

        for i in range(n):
            names[i] = look[heights[i]]

        return names
        