class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        p = sorted(processorTime)
        t = sorted(tasks, reverse=True)
        ans = 0
        e = 4
        s = 0
        for i in range(len(p)):
            maxx = 0   
            for j in range(s, e):
                if t[j] + p[i] > maxx:
                    maxx = t[j] + p[i]
            e += 4
            s += 4
            ans = max(ans, maxx)
        return ans
        