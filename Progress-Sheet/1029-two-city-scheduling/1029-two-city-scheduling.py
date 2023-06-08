class Solution(object):
    def twoCitySchedCost(self, costs):
        arr = sorted(costs, key = lambda x: x[1] - x[0])
        print(arr)
        sumA = 0
        sumB = 0
        for i in range(len(arr)//2):
            sumB += arr[i][1]         
        for i in range(len(arr)//2, len(arr)):
            sumA += arr[i][0]
        return sumA + sumB