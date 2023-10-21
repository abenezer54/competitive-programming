class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        D = [ arr[i+1] - arr[i] for i in range(len(arr)-1) ]
        target = min(D)
        res    = []
        for i,d in enumerate(D):
            if d == target:
                res.append([ arr[i],arr[i+1] ])
        return res
        