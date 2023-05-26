class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        
        def mycmp(a, b):
            if int(str(a) + str(b)) > int(str(b) + str(a)):
                return -1
            elif int(str(a) + str(b)) < int(str(b) + str(a)):
                return 1
            else:
                return 0
        nums.sort(key = cmp_to_key(mycmp))
        ans = ""
        if  int("".join(map(str,nums))) == 0:
            ans += "0"
        else:
            ans += "".join(map(str,nums)) 
        
        return ans