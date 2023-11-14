class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for path in paths:
            path = path.split()
            folder = path[0]
            for i in range(1, len(path)):
                theFile = path[i].split("(")[1][:-1]
                ans[theFile].append(folder + "/" + path[i].split("(")[0])

        return [value for value in ans.values() if len(value) > 1]
        