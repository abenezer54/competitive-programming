class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        arr = []
        for i in range(len(heights)):
            dic[heights[i]] = names[i]
        
        #Using Bubble Sort
        # for i in range(len(heights)):
        #     for j in range(len(heights) - 1):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
       
        heights.sort(reverse = True)
                
        for i in range(len(heights)):
            arr.append(dic[heights[i]])
        return arr
