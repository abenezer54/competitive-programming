class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = defaultdict(list)
        ans = []

        for i, num in enumerate(groupSizes):
            group[num].append(i)
            if len(group[num]) == num:
                ans.append(group[num])
                group[num] = []
         
        return ans
        