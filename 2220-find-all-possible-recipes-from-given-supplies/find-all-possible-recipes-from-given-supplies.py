class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        n = len(recipes)
        mp = {recipes[i]: i  for i in range(n)}
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for i in range(n):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] in supplies:
                    continue
                elif ingredients[i][j] in mp:
                    adj[mp[ingredients[i][j]]].append(i)
                    ind[i] += 1
                else:
                    ind[i] += 1
        ans = []
        que = deque()
        for i in range(n):
            if not ind[i]:
                que.append(i)
                ans.append(recipes[i])
        
        while que:
            node = que.popleft()
            for child in adj[node]:
                ind[child] -= 1
                if not ind[child]:
                    ans.append(recipes[child])
                    que.append(child)
        return ans
        