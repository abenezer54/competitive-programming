class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        arr = []
        for i in range(len(heights)):
            dic[heights[i]] = names[i]
        heights.sort(reverse = True)
        for i in range(len(heights)):
            arr.append(dic[heights[i]])
        return arr
