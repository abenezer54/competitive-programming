class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        arr1 = sorted([x for x in s1])
        arr2 = sorted([x for x in s2])
        print(arr1)
        print(arr2)
        ans1 = True
        for i in range(len(arr1)):
            if arr1[i] < arr2[i]:
                ans1 = False
                break
        print(ans1)
        ans2 = True
        for i in range(len(arr1)):
            if arr2[i] < arr1[i]:
                ans2 = False
                break
        ans = [ans1 , ans2]
        print(ans)
        return True if True in ans else False