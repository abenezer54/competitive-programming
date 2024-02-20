class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda task: (-(task[1] - task[0]), task[0]))
        n, ans, cur = len(tasks), 0, 0

        for i in range(n):
            if  cur < tasks[i][1]:
                ans +=  tasks[i][1] - cur
                cur = tasks[i][1] - tasks[i][0]
            else:
                cur -= tasks[i][0]
            
        return ans
        