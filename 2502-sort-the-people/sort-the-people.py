class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        look = {heights[i]:names[i] for i in range(len(names))}
        minn = min(heights)
        maxx = max(heights)
        
        count = [0] * (maxx - minn + 1)
        for i in range(n):
            count[heights[i] - minn] += 1

        new = [0] * n 
        cur = 0
        for j in range(len(count)):
            if count[j]:
                new[cur] = j + minn
                cur += count[j]     

        new.reverse()
        heights = new

        for i in range(n):
            names[i] = look[heights[i]]

        return names
