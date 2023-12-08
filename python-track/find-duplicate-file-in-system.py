class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for path in paths:
            directory, *files = path.split()
            for _file in files:
                num, key = _file.split("(")
                lookup[key[:-1]].append(directory +"/" + num)

        ans = []
        for value in lookup.values():
            if len(value) > 1:
                ans.append(value)

        return ans
        