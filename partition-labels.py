class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = Counter(s)
        temp = defaultdict(int)
        ans = []
        left = 0
        for right, char in enumerate(s):
            temp[char] += 1
            if all(temp[key] == dic[key] for key in temp.keys()):
                ans.append(right - left + 1)
                left = right + 1
                temp.clear()
        return ans