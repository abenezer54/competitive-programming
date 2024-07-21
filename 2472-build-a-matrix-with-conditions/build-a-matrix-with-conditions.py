class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowGraph,colGraph = defaultdict(list),defaultdict(list)

        for a,b in rowConditions: #O(n)
            rowGraph[b].append(a)

        for l,r in colConditions: #O(m)
            colGraph[r].append(l)

        def dfs(num,graph,visited,res):
            if num in visited:
                return visited[num]
            
            visited[num] = True
            for nei in graph[num]:
                if dfs(nei,graph,visited,res):
                    return True
            visited[num] = False
            res.append(num)

        rowOrder,colOrder = [],[]
        rowVisited,colVisited = {},{}
        for i in range(1,k+1): #O(k+(m+n))
            if dfs(i,rowGraph,rowVisited,rowOrder) or dfs(i,colGraph,colVisited,colOrder):
                return []

        colPos = defaultdict(int)
        for i,num in enumerate(colOrder):#O(k)
            colPos[num] = i

        matrix = [[0 for i in range(k)] for j in range(k)] #O(k^2)

        for index,r in enumerate(rowOrder):#O(k)
            j = colPos[r]
            matrix[index][j] = r
        
        return matrix
