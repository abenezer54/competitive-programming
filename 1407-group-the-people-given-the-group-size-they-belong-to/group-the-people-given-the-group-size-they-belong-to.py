class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = defaultdict(list)
        for i, num in enumerate(groupSizes):
            group[num].append(i)
            
        ans = []
        for key, value in group.items():
            if key < len(value):
                print(value)
                start = 0
                for end in range(key, len(value) + 1, key):
                    ans.append(value[start:end])
                    start += key     
            else:
                ans.append(value)
            
        return ans
        