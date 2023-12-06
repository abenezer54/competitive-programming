class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        idx = float("inf")
        for i in range(len(list1)):
            if list1[i] in list2:
                currentIndexSum = i + list2.index(list1[i])
                if currentIndexSum < idx:
                    ans.clear()
                    ans.append(list1[i])
                    idx = currentIndexSum
                elif currentIndexSum == idx:
                    ans.append(list1[i])
        return ans
        