class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        a = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        a.sort()
        cur, n, idx = 0, len(tasks), 0
        ava, ans = [], []

        while len(ans) != n:
            while idx < n and cur >= a[idx][0]:
                heappush(ava, (a[idx][1], a[idx][2]))
                idx += 1

            if not ava:
                val = a[idx][0]  
                while idx < n and val == a[idx][0]:
                    heappush(ava, (a[idx][1], a[idx][2]))
                    idx += 1      
                cur = val
            task = heappop(ava)
            ans.append(task[1])
            cur += task[0]
        
        return ans
