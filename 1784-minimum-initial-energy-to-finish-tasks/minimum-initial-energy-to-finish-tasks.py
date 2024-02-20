class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda task: (-(task[1] - task[0]), task[0]))
        n, ans, cur = len(tasks), 0, 0

        for actual, minimum in tasks:
            if  cur < minimum:
                ans +=  minimum - cur
                cur = minimum - actual
            else:
                cur -= actual
            
        return ans
        