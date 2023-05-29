class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(r)):
            arr = sorted(nums[l[i]:r[i]+1])
            d = arr[1] - arr[0]
            if len(arr) < 2:
                ans.append(False)
            elif len(arr) == 2:
                ans.append(True)
            else:
                isArithmetic = False
                for j in range(2, len(arr)):
                    if arr[j] - arr[j -1] == d:
                        isArithmetic = True
                    else:
                        isArithmetic = False
                        break
                if isArithmetic:
                    ans.append(True) 
                else:
                    ans.append(False)
        return ans