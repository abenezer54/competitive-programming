class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        
        ans = 0
        for i in range(len(tasks)):
            ans = max(ans, tasks[i] + processorTime[i // 4])

        return ans
        